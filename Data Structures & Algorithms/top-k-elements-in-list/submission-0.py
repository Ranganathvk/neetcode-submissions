
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        count_map = dict(Counter(nums))
        top_k = dict(sorted(count_map.items(), key=lambda x: x[1], reverse=True)[:k])
        return list(top_k.keys())

