from backspace_compare import backspace_compare
import pytest


@pytest.mark.parametrize("input_data,expected_result", [
    (["ab#c", "ad#c"], True),
    (["ab##", "c#d#"], True),
    (["a##c", "#a#c"], True),
    (["a#c", "b"], False),
])
def test_backspace_compare(input_data, expected_result):
    actual_result = backspace_compare(*input_data)
    assert actual_result == expected_result
