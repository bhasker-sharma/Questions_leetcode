class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map ={}
        for str in strs:
            result = "".join(sorted(str))
            if result in map:
                map[result].append(str)
            else:
                map[result] = [str]
        return list(map.values())



        