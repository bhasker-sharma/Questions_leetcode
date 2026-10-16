class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}
        ans = []
        for i,num in enumerate(nums):
            to_find = target-num
            if to_find in map:
                return [map[to_find], i]
            else:
                map[num] = i
        return ans

        