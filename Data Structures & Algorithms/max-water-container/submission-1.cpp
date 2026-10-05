class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_area = 0;
        int i = 0;
        int j = heights.size()-1;
        while(i<j){
            int curr_area = (j-i) * min(heights[i],heights[j]);
            if (heights[i]<heights[j]){
                i++;
            }
            else{
                j--;
            }
            max_area = max(max_area,curr_area);
        }
        return max_area;
    }
};
