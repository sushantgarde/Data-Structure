class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        print(freq)
        freq = sorted(freq, key = lambda x: -freq[x])
        print(freq)
        result = [0]*k
        for i in range(k):
            result[i] = freq[i]
            print(result)

        return result