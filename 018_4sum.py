# sort input and use nested loop , i starts 0 ends len(nums)-4 , j starts i + 1 ends len(nums) - 3
# set two pointer find two more digits add to nums at index of i and j to match the target, 
# push to target or increment on of the pointer depends on the sum 
# use while loop skip duplicates on each loop

# time: O(n^3)
# space: O(log n)

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort() 

        for i in range(len(nums) - 3): 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue 
            for j in range(i + 1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j - 1]: 
                    continue 
                k = j+1 
                l = len(nums) - 1
                while k < l: 
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1 
                        l -= 1 
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sum < target: 
                        k += 1
                    else: 
                        l -= 1 
        return res
