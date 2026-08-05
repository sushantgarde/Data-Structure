class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums1 = []
        # for i in nums:
        #     if i in nums1:
        #         return i
        #     else:
        #         nums1.append(i)
        nums.sort()
        temp = nums[0]
        for i in range(1,len(nums),1):
            if temp == nums[i]:
                return nums[i]
            else:
                temp = nums[i
                ]