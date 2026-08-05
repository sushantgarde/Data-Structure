class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != last:
                nums[index] = nums[i]
                index+=1
                last = nums[i]
        return index