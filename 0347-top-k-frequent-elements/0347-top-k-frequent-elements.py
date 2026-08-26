class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        freq = sorted(freq, key = lambda x: -freq[x])
        result = [0]*k
        for i in range(k):
            result[i] = freq[i]

        return result