class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # store indices
        max_length = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    length = i - stack[-1]  # current index - last index stored
                    max_length = max(max_length, length)

        return max_length