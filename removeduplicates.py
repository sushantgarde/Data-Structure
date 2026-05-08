nums = [0,0,1,1,1,2,2,3,3,4]
index = 1
last = nums[0]
for i in range(1, len(nums)):
    if nums[i] != last:
        nums[index] = nums[i]
        index+=1
        last = nums[i]
print( index)