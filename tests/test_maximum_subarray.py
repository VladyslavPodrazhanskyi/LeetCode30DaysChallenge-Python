from maximum_subarray import max_sub_array_sum
import pytest


@pytest.mark.parametrize("input_data,output_data", [
    ([4, -1, 2, 1], 6),
    ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
    ([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7], -3)
])
def test_max_sub_array_sum(input_data, output_data):
    result = max_sub_array_sum(input_data)
    assert output_data == result
