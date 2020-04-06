import pytest

from group_anagrams import group_anagrams


@pytest.mark.parametrize("input_data,output_data", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [
        ["ate", "eat", "tea"],
        ["nat", "tan"],
        ["bat"]
    ]),
    (["qwe", "klj"], [["qwe"], ["klj"]]),
    ([], [])
])
def test_group_anagrams(input_data, output_data):
    result = group_anagrams(input_data)
    assert output_data == result
