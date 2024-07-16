from typing import List

# set two pointer to be 1 loop array(first element doesnt matter), right++ if duplicate with last element, else set nums[left] to be nums[right] and update both pointer 
# return left pointer,(uniq element + 1), and array become uniq in beginning 

#time: O(n)
#space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        left, right = 1, 1 
        while right < len(nums): 
            if nums[right] == nums[right - 1]:
                right += 1 
            else:
                nums[left] = nums[right] 
                left+=1 
                right+=1 
        return left
