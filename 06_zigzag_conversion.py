# // if s.length  = 1 or length < numRows, return s 
#  // initial res and indexJump( numRows * 2 - 2 ) 
#  // loop numRows 
#  // set i = row midIndexJump (if not first and last row, need add the mid char)
#  // midIndexJump = indexJump - 2 * currentRow (v shape; row starts 0 so - 2)
#  // while i < s.length, res add s[i] and if its not first or last row and the  i + midindex is in bounce, means there is a mid char, add that cahr s[i + midIndexJump]

#  // time: O(n) 
#  // space O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or len(s) < numRows: 
            return s 
        
        res = '' 
        index_jump = numRows * 2 - 2 
        
        for row in range(numRows):
            mid_index_jump = index_jump - 2 * row
            for i in range(row,len(s), index_jump):
                res += s[i] 

                if row > 0 and row < numRows - 1 and i + mid_index_jump < len(s):
                    res += s[i + mid_index_jump]

        return res
