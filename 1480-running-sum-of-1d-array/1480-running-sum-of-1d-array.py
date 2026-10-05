class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # sum = 0 
        # for i in range(len(nums)):
        #     nums[i] = sum + nums[i]
        #     sum = nums[i]
        # return nums
        t=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            t.append(sum)
        return t
        