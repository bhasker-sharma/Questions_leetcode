class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        max_area  = 0
        heights.append(0)
        for i,height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                popped_height = heights[stack.pop()]
                right_bauder = i
                if stack:
                    left_bauder = stack[-1]
                    width = right_bauder-left_bauder -1
                else:
                    width = right_bauder
                current_area = width * popped_height
                max_area = max(max_area,current_area)
            
            stack.append(i)
        return max_area

        
        