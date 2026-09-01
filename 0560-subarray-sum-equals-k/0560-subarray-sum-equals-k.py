class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute foce
        # count = 0

        # for i in range(len(nums)):
        #     total = 0

        #     for j in range(i, len(nums)):
        #         total += nums[j]

        #         if total == k:
        #             count += 1

        # return count

        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            required = prefix_sum - k

            if required in prefix_count:
                count += prefix_count[required]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count