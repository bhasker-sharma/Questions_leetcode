class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans =[]

        for i ,val in enumerate(nums):
            j = i+1
            k = len(nums) - 1
            if i >0 and nums[i] == nums[i-1]:
                continue 
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum < 0:
                    j += 1
                elif current_sum > 0:
                    k -= 1
                elif current_sum == 0:
                    to_add = [val,nums[j],nums[k]]
                    ans.append(to_add)
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
        return ans
