"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [1,2,3,4]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    O(n^2)
    :param nums:
    :return:
    """
    length = len(nums)

    answer = [1] * length

    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            answer[i] *= nums[j]

    return answer


def product_except_self(nums: List[int]) -> List[int]:
    """
    O(n)
    :param nums:
    :return:
    """
    length = len(nums)

    answer = [0] * length
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    right_element = 1
    for i in reversed(range(length)):
        answer[i] = answer[i] * right_element
        right_element *= nums[i]

    return answer
