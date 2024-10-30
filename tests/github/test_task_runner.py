# Copyright (C) 2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import os
import time
import socket
import argparse
from pathlib import Path
from subprocess import check_call
from concurrent.futures import ProcessPoolExecutor

from openfl.utilities.utils import rmtree, getfqdn_env
from tests.github.utils import create_collaborator, initialize_and_certify_workspace, certify_aggregator


if __name__ == '__main__':
    # Test the pipeline
    parser = argparse.ArgumentParser()
    parser.add_argument('--workspace', default='fed_work12345alpha81671')
    parser.add_argument('--col1', default='one123dragons')
    parser.add_argument('--col2', default='beta34unicorns')
    parser.add_argument('--rounds-to-train')
    parser.add_argument('--col1-data-path', default='1')
    parser.add_argument('--col2-data-path', default='2')
    parser.add_argument('--save-model')

    origin_dir = Path.cwd().resolve()
    args = parser.parse_args()
    workspace = args.workspace
    archive_name = f'{workspace}.zip'
    fqdn = getfqdn_env()
    rounds_to_train = args.rounds_to_train
    col1, col2 = args.col1, args.col2
    col1_data_path, col2_data_path = args.col1_data_path, args.col2_data_path
    save_model = args.save_model

    # START
    # =====
    # Make sure you are in a Python virtual environment with the FL package installed.
    initialize_and_certify_workspace(workspace, fqdn, rounds_to_train)
    certify_aggregator(fqdn)

    workspace_root = Path().resolve()  # Get the absolute directory path for the workspace

    # Create collaborator #1
    create_collaborator(col1, workspace_root, col1_data_path, archive_name, workspace)

    # Create collaborator #2
    create_collaborator(col2, workspace_root, col2_data_path, archive_name, workspace)

    # Run the federation
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.submit(check_call, ['fx', 'aggregator', 'start'], cwd=workspace_root)
        time.sleep(5)

        dir1 = workspace_root / col1 / workspace
        executor.submit(check_call, ['fx', 'collaborator', 'start', '-n', col1], cwd=dir1)

        dir2 = workspace_root / col2 / workspace
        executor.submit(check_call, ['fx', 'collaborator', 'start', '-n', col2], cwd=dir2)

    os.chdir(origin_dir)
    rmtree(workspace_root)
