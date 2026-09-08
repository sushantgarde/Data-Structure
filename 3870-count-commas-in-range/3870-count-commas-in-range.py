class Solution:
    def countCommas(self, n: int) -> int:
        # if n < 1000:
        #     return 0
        # return (n-999)

        return (max(n-999, 0))

        