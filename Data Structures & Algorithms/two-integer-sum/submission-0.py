class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}
        for idx,digit in enumerate(nums):
            to_find= target-digit
            if to_find in map:
                return [map.get(to_find),idx]
            else:
                map[digit] = idx