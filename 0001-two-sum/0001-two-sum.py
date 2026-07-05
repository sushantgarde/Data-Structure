class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store the numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num  # The value that we need to find
            if complement in num_map:  # Check if complement exists in the map
                return [num_map[complement], i]  # Return the indices of the two numbers
            num_map[num] = i  # Add the current number to the map
