from single_number import single_number, single_number_math
import pytest


@pytest.mark.parametrize("input_data,output_data,test_function",
                         [([2, 2, 3, 1, 4, 3, 4], 1, single_number),
                          ([2, 2, 3, 1, 4, 3, 4], 1, single_number_math),
                          ([1, 1, 2, 2, 3], 3, single_number),
                          ([1, 1, 2, 2, 3], 3, single_number_math),
                          ([3, 2, 2, 1, 1], 3, single_number),
                          ([3, 2, 2, 1, 1], 3, single_number_math),
                          ],
                         )
def test_single_number(input_data, output_data, test_function):
    for i in range(len(input_data)):
        result = test_function(input_data)
        assert result == output_data
