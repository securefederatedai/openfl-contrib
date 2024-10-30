# Copyright (C) 2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""CustomWeightedAverage tests."""

import pytest
import numpy as np

from openfl.databases.tensor_db import TensorDB
from openfl.utilities.types import TensorKey

from openfl_contrib.interface.aggregation_functions import CustomWeightedAverage


@pytest.fixture
def tensor_db():
    """Prepare tensor db."""
    db = TensorDB()
    array_1 = np.array([0, 1, 2, 3, 4])
    tensor_key_1 = TensorKey(tensor_name='tensor',  origin= '', round_number=0, report=False, tags=('col1',))
    array_2 = np.array([5, 6, 7, 8, 9])
    tensor_key_2 = TensorKey(tensor_name='tensor',  origin= '', round_number=0, report=False, tags=('col2',))
    db.cache_tensor({
        tensor_key_1: array_1,
        tensor_key_2: array_2
    })
    return db


def test_get_aggregated_tensor_weights(tensor_db):
    """Test that get_aggregated_tensor calculates correctly."""

    collaborator_weight_dict = {
        'col1': 0.9, 
        'col2': 0.1
        }

    tensor_key = TensorKey(tensor_name='tensor',  origin= '', round_number=0, report=False, tags=())

    agg_nparray = tensor_db.get_aggregated_tensor(
        tensor_key, collaborator_weight_dict, CustomWeightedAverage())

    control_nparray = np.average(
        [np.array([0, 1, 2, 3, 4]), np.array([5, 6, 7, 8, 9])],
        weights=np.array(list(collaborator_weight_dict.values())),
        axis=0
    )

    assert np.array_equal(agg_nparray, control_nparray)