from typing import List
# // two pointer loop nums, if current element  != val, move it to curr pointer, increment curr, return curr after loop

# //time:O(n)
# //space:O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0 

        for i in range(len(nums)): 
            if nums[i] != val:
                nums[curr] = nums[i] 
                curr += 1 
        return curr