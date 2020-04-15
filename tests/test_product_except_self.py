from product_of_erray_except_self import product_except_self
import pytest


@pytest.mark.parametrize("input_data,output_data", [
    ([1, 2, 3, 4], [24, 12, 8, 6])
])
def test_move_zeros(input_data, output_data):
    result = product_except_self(input_data)
    assert output_data == result
