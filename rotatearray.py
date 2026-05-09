def rotate(nums, k):
    # n = len(nums)
    # k = k % n
    #
    # for j in range(k):
    #     temp = nums[n - 1]
    #
    #     for i in range(n - 1, 0, -1):
    #         nums[i] = nums[i - 1]
    #
    #     nums[0] = temp
    n = len(nums)
    k %= n

    temp = []

    # store last k elements
    for i in range(n - k, n):
        temp.append(nums[i])

    # shift remaining elements right
    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]

    # place temp elements at beginning
    for i in range(k):
        nums[i] = temp[i]
    return nums
print(rotate([1,2,3,4,5,6,7],3))