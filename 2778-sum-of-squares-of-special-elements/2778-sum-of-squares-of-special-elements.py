class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(1,n+1):
            if n % i == 0 :
                i = i-1
                result = result + (nums[i] * nums[i])
        return result