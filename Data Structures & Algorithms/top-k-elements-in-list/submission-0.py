from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        x = count.most_common(k)
        
        return [num[0] for num in x]
