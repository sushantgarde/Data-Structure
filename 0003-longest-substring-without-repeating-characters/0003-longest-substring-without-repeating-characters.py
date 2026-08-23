class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        count = 0
        ans_count = 0

        for char in s:
            if char in stack:
                while char in stack:
                    stack.pop(0)
                    count -= 1

            stack.append(char)
            count += 1
            ans_count = max(ans_count, count)
        return ans_count