from itertools import permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute force approach
        '''perm = sorted(set(permutations(nums)))
        curr = tuple(nums)
        idx = perm.index(curr)

        if idx == len(perm) - 1:
            nums[:] = perm[0]
        else:
            nums[:] = perm[idx + 1]
        '''
         
        # Optimal Solution
        #Setting the index as -1
        set_index = -1
        #Finding the decreasing points
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                set_index = i
                break
        #if no smallest is found then reverse the list
        if set_index == -1:
            nums.reverse()
            return
        # finding the slightly grater number
        for i in range(len(nums) - 1, set_index, -1):
            if nums[i] > nums[set_index]:
                # Swap them
                nums[i], nums[set_index] = nums[set_index], nums[i]
                break

        #Revesed the part after the index
        nums[set_index + 1:] = reversed(nums[set_index + 1:])