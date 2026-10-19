class Solution:
    def maxProduct(self, n: int) -> int:
        digit = []
        while n > 0:
            digits = n%10
            digit.append(digits)
            n = n//10
        # print(digit)
        digit.sort()
        # print(digit)
        return digit[-2] * digit[-1]