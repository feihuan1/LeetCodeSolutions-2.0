# // sort array, set defaul res 
# // loop array skip duplicates 
# // set two pointer between next index and end  
# // if sum equal target means distance is 0, return it, else, update res if sum is closer to target 
# // move pointer depends if sum is too small or too big


# // time O(n^2)
# // space: O(log n)


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        res = nums[0] + nums[1] + nums[2] 
        nums.sort()
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            j = i + 1 
            k = len(nums) - 1
            while(j < k):
                sum = nums[i] + nums[j] + nums[k] 
                
                if sum == target: 
                    return sum 
                if abs(target - sum) < abs(target - res): 
                    res = sum 
                
                if(sum < target):
                    j += 1
                else:
                    k -= 1

        
        
        return res 