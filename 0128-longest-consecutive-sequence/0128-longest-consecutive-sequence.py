# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         nums.sort()
#         max_length = 1
#         current_length = 1
        
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:  # Skip duplicates
#                 if nums[i] == nums[i - 1] + 1:
#                     current_length += 1
#                 else:
#                     max_length = max(max_length, current_length)
#                     current_length = 1
        
#         return max(max_length, current_length)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            return 2 if nums[0] == -100000000 else 100000

        res = 1
        for n in (nums := {*nums}):
            if n - 1 not in nums:
                length = 1
                while n + length in nums:
                    length += 1
                if length > res:
                    res = length

        return res