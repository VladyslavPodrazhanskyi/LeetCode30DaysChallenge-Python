from best_time_to_buy_and_sell_stock import max_profit
import pytest


@pytest.mark.parametrize("input_data,output_data", [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0)
])
def test_max_profit(input_data, output_data):
    result = max_profit(input_data)
    assert output_data == result
