from move_zeros import move_zeros
import pytest


@pytest.mark.parametrize("input_data,output_data", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, 0, 0, 1], [1, 0, 0, 0]),
    ([0, 0, 0], [0, 0, 0]),
    ([1, 2, 3], [1, 2, 3])
])
def test_move_zeros(input_data, output_data):
    move_zeros(input_data)
    assert output_data == input_data
