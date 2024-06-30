# loop through array and set two pointer to be next element and last element 
# if duplicate, skip current loop 
# if sum is 0 append it to res

# time: O(n^2)
# space: O(n^2)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = [] 
        nums.sort() 

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1 
            k = len(nums) - 1

            while j < k: 
                
                sum = nums[i] + nums[j] + nums[k] 

                if sum > 0:
                    k -= 1 
                elif sum < 0: 
                    j += 1 
                else: 
                    res.append([nums[i], nums[j], nums[k]] )  
                    while j < k and nums[j] == nums[j + 1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]: 
                        k -= 1
                    j += 1
                    k -= 1
        
        return res

