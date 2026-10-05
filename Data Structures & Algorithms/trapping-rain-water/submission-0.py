class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1
        left_max = 0
        right_max =0
        ans =0
        while i<j:
            left_max = max(height[i],left_max)
            right_max = max(height[j],right_max)
            if left_max < right_max:
                ans += left_max -height[i]
                i+=1
            else:
                ans += right_max - height[j]
                j-=1
        return ans
        