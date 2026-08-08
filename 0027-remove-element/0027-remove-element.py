class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Brute Force
        # count = 0
        # if not nums:
        #     return count
        # og = []
        # for num in nums:
        #     if num == val:
        #         count += 1
        #     else:
        #         og.append(num)
        # for i in range(len(og)):
        #     nums[i] = og[i]
        
        # return len(og)

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k