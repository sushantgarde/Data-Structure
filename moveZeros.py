nums = [0,1,0,3,12]

j = 0  # position for non-zero

for i in range(len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]
        j += 1

# fill remaining with 0
for i in range(j, len(nums)):
    nums[i] = 0

print(nums)