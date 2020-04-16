"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:

Input: "()"
Output: True
Example 2:

Input: "(*)"
Output: True
Example 3:

Input: "(*))"
Output: True

"""


def check_valid_string(s: str) -> bool:
    lo = hi = 0
    for char in s:
        lo += 1 if char == '(' else -1
        hi += 1 if char != ')' else -1
        if hi < 0:
            break
        lo = max(lo, 0)

    return lo == 0
