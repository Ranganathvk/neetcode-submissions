class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        sorts=sorted(s)
        sortt=sorted(t)
        
        if sorts == sortt:
           return True
        else:
            return False


        