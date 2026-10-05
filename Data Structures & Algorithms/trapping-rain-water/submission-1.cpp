class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        int i = 0;
        int j = height.size() -1;
        int left_max =0;
        int right_max =0;
        while(i<j){
            left_max = max(left_max,height[i]);
            right_max = max(right_max,height[j]);
            if(left_max<right_max){
                ans += left_max -height[i];
                i++;
            }
            else{
                ans += right_max -height[j];
                j--;
            }
        }
        return ans;
    }
};
