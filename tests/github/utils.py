# Copyright (C) 2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
import shutil
from subprocess import check_call
import os
from pathlib import Path
import re


def create_collaborator(col, workspace_root, data_path, archive_name, fed_workspace):
    # Copy workspace to collaborator directories (these can be on different machines)
    col_path = workspace_root / col
    shutil.rmtree(col_path, ignore_errors=True)  # Remove any existing directory
    col_path.mkdir()  # Create a new directory for the collaborator

    # Import the workspace to this collaborator
    check_call(
        ['fx', 'workspace', 'import', '--archive', workspace_root / archive_name],
        cwd=col_path
    )

    # Create collaborator certificate request
    check_call(
        ['fx', 'collaborator', 'create', '-d', data_path, '-n', col, '--silent'],
        cwd=col_path / fed_workspace
    )
    # Remove '--silent' if you run this manually
    check_call(
        ['fx', 'collaborator', 'generate-cert-request', '-n', col, '--silent'],
        cwd=col_path / fed_workspace
    )

    # Sign collaborator certificate
    # Remove '--silent' if you run this manually
    request_pkg = col_path / fed_workspace / f'col_{col}_to_agg_cert_request.zip'
    check_call(
        ['fx', 'collaborator', 'certify', '--request-pkg', str(request_pkg), '--silent'],
        cwd=workspace_root)

    # Import the signed certificate from the aggregator
    import_path = workspace_root / f'agg_to_col_{col}_signed_cert.zip'
    check_call(
        ['fx', 'collaborator', 'certify', '--import', import_path],
        cwd=col_path / fed_workspace
    )


def initialize_and_certify_workspace(path, fqdn, rounds_to_train):
    path = os.path.join('openfl_contrib_workspace', path)
    os.chdir(path)

    ("save").mkdir(exist_ok=True)
    ("local_state").mkdir(exist_ok=True)

    check_call(['pip', 'install', '-r', 'requirements.txt'])

    # Initialize FL plan
    check_call(['fx', 'plan', 'initialize', '-a', fqdn])
    plan_path = Path('plan/plan.yaml')
    try:
        rounds_to_train = int(rounds_to_train)
        with open(plan_path, "r", encoding='utf-8') as sources:
            lines = sources.readlines()
        with open(plan_path, "w", encoding='utf-8') as sources:
            for line in lines:
                sources.write(
                    re.sub(r'rounds_to_train.*', f'rounds_to_train: {rounds_to_train}', line)
                )
    except (ValueError, TypeError):
        pass
    # Create certificate authority for workspace
    check_call(['fx', 'workspace', 'certify'])

    # Export FL workspace
    check_call(['fx', 'workspace', 'export'])


def certify_aggregator(fqdn):
    # Create aggregator certificate
    check_call(['fx', 'aggregator', 'generate-cert-request', '--fqdn', fqdn])

    # Sign aggregator certificate
    check_call(['fx', 'aggregator', 'certify', '--fqdn', fqdn, '--silent'])
