// two pointer loop nums, if current element  != val, move it to curr pointer, increment curr, return curr after loop

//time:O(n)
//space:O(1)

public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int curr = 0; 
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] != val)
            {
                nums[curr] = nums[i]; 
                curr++;
            }
        }
        return curr;
    }
}