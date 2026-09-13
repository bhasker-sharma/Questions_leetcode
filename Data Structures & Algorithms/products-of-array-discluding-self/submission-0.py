class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans =[1]*len(nums)
        running_left = 1
        running_right = 1
        for i in range(len(nums)):
            ans[i] = running_left
            running_left = running_left * nums[i] 
        for j in range(len(nums)-1,-1,-1):
            ans[j] = ans[j] * running_right
            running_right = running_right * nums[j]
        return ans       