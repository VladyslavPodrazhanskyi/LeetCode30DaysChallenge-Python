from happy_number import is_happy
import pytest


@pytest.mark.parametrize("input_data,output_data", [(19, True), (125, False), (1, True)], )
def test_happy_number(input_data, output_data):
    result = is_happy(input_data)
    assert result == output_data
