"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    hasp_map = defaultdict(list)
    for s in strs:
        hasp_map[tuple(sorted(s))].append(s)
    result = [sorted(elem) for elem in hasp_map.values()]
    return result
