class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = dict(Counter(nums))
        result = []
    # print(freq)
        for num, count in freq.items():
            if count > len(nums)//3:
                result.append(num)
        
        return (result)