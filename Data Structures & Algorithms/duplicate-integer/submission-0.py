class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        my_hashmap = {}
        for num in nums:
            if my_hashmap.get(num) is None:
               my_hashmap[num]=1
            else:
              return True

        return False  
        