from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [] 

        def backtrack(s='', openC=0, closeC=0):
            if len(s) == n*2:
                result.append(s) 
                return 
            
            if openC < n:
                backtrack(s+"(", openC+1, closeC) 

            if closeC < openC: 
                backtrack(s+")", openC, closeC+1)
        backtrack()
        return result