import numpy as np
import pytest

from openfl.protocols import base_pb2
from openfl_contrib.pipelines import SKCPipeline


@pytest.fixture
def named_tensor():
    """Initialize the named_tensor mock."""
    tensor = base_pb2.NamedTensor(
        name='tensor_name',
        round_number=0,
        lossless=False,
        report=False,
        data_bytes=32 * b'1'
    )
    metadata = tensor.transformer_metadata.add()
    metadata.int_to_float[1] = 1.
    metadata.int_list.extend([1, 8])
    metadata.bool_list.append(True)

    return tensor


def test_skc_compression_pipeline(named_tensor):
    """Test that SKCPipeline works correctly."""

    tp = SKCPipeline()
    proto = named_tensor.transformer_metadata.pop()
    metadata = {'int_to_float': proto.int_to_float,
                'int_list': proto.int_list,
                'bool_list': proto.bool_list
                }
    array_shape = tuple(metadata['int_list'])
    flat_array = np.frombuffer(named_tensor.data_bytes, dtype=np.float32)

    nparray = np.reshape(flat_array, newshape=array_shape, order='C')

    data_fwd, transformer_metadata = tp.forward(nparray)
    assert len(transformer_metadata) == 3
    assert isinstance(data_fwd, bytes)

    data_bwd = tp.backward(data_fwd, transformer_metadata)
    assert data_bwd.shape == tuple(metadata['int_list'])
