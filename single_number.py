from collections import defaultdict
from typing import List

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity.

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""


def single_number(input_data: List[int]) -> int:
    hash_map = defaultdict(int)

    for elem in input_data:
        hash_map[elem] += 1

    for key, value in hash_map.items():
        if value == 1:
            return key


def single_number_math(input_date: List[int]) -> int:
    return 2 * sum(set(input_date)) - sum(input_date)
