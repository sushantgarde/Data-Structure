class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        # print(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        if len(result) == 0:
            return []
        else:
            return result