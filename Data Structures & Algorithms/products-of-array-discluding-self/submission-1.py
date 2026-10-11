class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left_ptr = 1
        right_ptr = 1
        for i in range(len(nums)):
            ans[i] = left_ptr
            left_ptr = left_ptr * nums[i]
        for j in range(len(nums)-1,-1,-1):
            ans[j] = ans[j]*right_ptr
            right_ptr = right_ptr * nums[j]
        return ans