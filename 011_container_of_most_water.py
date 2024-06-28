 # // brute force will be loop in loop O(n^2)

# // two pointer approach 

# // set two pointer i, j on each side of array , res initial to 0 
# // loop arr while i < j 
# // w * h is current container size w = j - i, h will be height[i] or height[j] witchever smaller 
# // update res if w * h is bigger 
# // move one pointer to center if that array value at index of pointer is smaller than other

#  // time: O(n) 
#  // space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, res = 0, len(height) - 1, 0 

        while l < r:
            area = (r - l) * min(height[l], height[r]) 
            res = max(res, area) 

            if height[l] < height[r]: 
                l += 1 
            else: 
                r -= 1 
        
        return res