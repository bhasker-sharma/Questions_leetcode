class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i =0    
        j = len(heights) - 1
        max_area =0
        while i<j:
            width = j-i
            curr_area = (width) * min(heights[i],heights[j])
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            max_area =max(max_area,curr_area)
        return max_area


        