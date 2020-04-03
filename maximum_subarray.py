"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


def max_sub_array_sum(a):
    max_sum = a[0]
    max_current = a[0]

    for i in range(1, len(a)):
        max_current = max(a[i], max_current + a[i])
        max_sum = max(max_current, max_sum)
    return max_sum
