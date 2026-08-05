class Solution:
    def maxSubArray(self, nums):
        # Brute force Approach
        # maximum = float('-inf')

        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         current_sum = 0
        #         for k in range(i, j+1):
        #             current_sum += nums[k]

        #         maximum = max(maximum, current_sum)

        # return maximum

        # Better approch
        # for i in range(len(nums)):
        #     current_sum = 0
        #     for j in range(i, len(nums)):
                
        #         current_sum += nums[k]

        #         maximum = max(maximum, current_sum)

        # return maximum

        # Best Approach
        curr_sum = 0
        maxi = float('-inf')
        for i in range(len(nums)):
            curr_sum += nums[i]
            maxi = max(maxi, curr_sum)
            if curr_sum <0 :
                curr_sum = 0
        return maxi