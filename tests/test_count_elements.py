from count_elements import count_elements
import pytest


@pytest.mark.parametrize("input_data,output_data", [
    ([1, 2, 3], 2),
    ([1, 1, 3, 3, 5, 5, 7, 7], 0),
    ([1, 3, 2, 3, 5, 0], 3),
    ([1, 1, 2, 2], 2),
    ([1, 1, 2], 2)
])
def test_max_sub_array_sum(input_data, output_data):
    result = count_elements(input_data)
    assert output_data == result
