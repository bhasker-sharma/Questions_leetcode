class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        return False if len(nums) == len(n) else True
        