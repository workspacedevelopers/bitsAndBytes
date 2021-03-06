"""
Leetcode:
https://leetcode.com/problems/valid-parentheses/

Question:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
	1. Open brackets must be closed by the same type of brackets.
	2. Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:    
            if c in ('(', '{', '['): 
                stack.append(c)

            else:
                if stack == []: 
                    return False
                elif c == ')' and stack[-1] == '(': 
                    stack.pop(-1)
                elif c == '}' and stack[-1] == '{':
                    stack.pop(-1)
                elif c == ']' and stack[-1] == '[':
                    stack.pop(-1)

                else:
                    return False

        if stack == []: 
            return True

        else: 
            return False

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
