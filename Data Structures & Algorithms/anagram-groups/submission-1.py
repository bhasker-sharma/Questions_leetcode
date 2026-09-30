class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map ={}
        for idx,value in enumerate(strs):
            res = "".join(sorted(value))
            if res in map:
                map[res].append(value)
            else:
                map[res] = [value]
        return list(map.values())