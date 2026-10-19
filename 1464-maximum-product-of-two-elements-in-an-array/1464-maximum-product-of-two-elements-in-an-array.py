class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        i = nums[-2]-1
        j = nums[-1]-1
        return (i*j)