def twoSum(nums, target):
    d = {}
    ledn = len(nums)
    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in d:
            return [d[needed], i]

        d[nums[i]] = i

print(twoSum([1,3,5,7,3,2], 9))