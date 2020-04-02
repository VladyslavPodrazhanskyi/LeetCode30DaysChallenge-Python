from collections import defaultdict

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""


def is_happy(n: int) -> bool:
    has_map = defaultdict(int)

    while n != 1:
        current = n
        sum_value = 0

        while current != 0:
            sum_value += pow(current % 10, 2)
            current //= 10

        if has_map[sum_value]:
            return False

        n = sum_value
        has_map[sum_value] = sum_value
    return True
