class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in hash_map:
                hash_map[char] += 1#add one more to the existing value
            else:
                hash_map[char] = 1
        for char in t:
            if char in hash_map:
                hash_map[char] -= 1
                if hash_map[char] ==0:
                    hash_map.pop(char)
            else:
                return False
        if len(hash_map) == 0:
            return True
        else:
            return False 