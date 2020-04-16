from check_valid_string import check_valid_string
import pytest


@pytest.mark.parametrize("input_data,expected_result", [
    ("()", True),
    ("(*)", True),
    ("(*))", True),
    ("())", False),
    ("(()", False),
])
def test_check_valid_string(input_data, expected_result):
    actual_result = check_valid_string(input_data)
    assert expected_result == actual_result
