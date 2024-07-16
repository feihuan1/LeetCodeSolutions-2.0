// # set two pointer to be 1 loop array(first element doesnt matter), right++ if duplicate with last element, else set nums[left] to be nums[right] and update both pointer 
// # return left pointer,(uniq element + 1), and array become uniq in beginning 

// #time: O(n)
// #space: O(1)


public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if(nums.Length <= 1) 
        {
            return nums.Length;
        }
        int curr = 1;

        for(int i = 1; i < nums.Length; i++) {
            if(nums[i] != nums[i - 1])
            {
                nums[curr] = nums[i]; 
                curr ++;
            }
        } 
        return curr;
    }
}