class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = {}
        for i in s:
            if i in l1:
                l1[i] += 1
            else:
                l1[i] = 1
        for j in t:
            if j in l1:
                l1[j] -= 1
                if l1[j] == 0:
                    l1.pop(j)
            else:
                return False
        if len(l1) == 0:
            return True 
        else:
            return False
            
        
        
        