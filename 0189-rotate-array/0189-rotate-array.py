class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute approach
        '''
        n = len(nums)
        k = k % n

        for j in range(k):
            temp = nums[n - 1]

            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]

            nums[0] = temp
        '''
        # Optimal Solution 
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