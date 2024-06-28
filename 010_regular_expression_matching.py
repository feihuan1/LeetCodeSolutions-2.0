# use dynamic programing 
# define dp dictionary 
# make recursive func 
# 3 base case: if (i,j) in dp, return it , if both str out of bounce(has to be >=len()), it true, if p out of bounce, it's false for sure, (i out of bounce might be true because p end with char + * could be None) 
# define match, i must in bounce , si = pj or pj = .!!
# check if next char of Pj is a *, (next cahr of pj has to in bounce)
# if it is, set cache of (i,j) to be recur(i, j+ 2)[dont use *] or (match[if use *, first char has to be the same] and recur(i + 1, p)[use *]) -> return cache at (i, j)
# if not *, check if match, set cache[(i,j)] to be move both pointer forward 
# if nothing happen, cache[(i,j)] = false and return false 

# just return dp(0,0)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {} 

        def recur(i, j):
            if (i, j) in dp:
                return dp[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True 
            if j >= len(p): 
                return False 

            match = i < len(s) and (s[i] == p[j] or p[j] == ".") 

            if j + 1 < len(p) and p[j + 1] == "*": 
                dp[(i, j)] = recur(i, j+ 2) or (match and recur(i + 1, j))
                return dp[(i, j)] 
            if match: 
                dp[(i, j)] = recur(i + 1, j + 1) 
                return dp[(i, j)]
            dp[(i, j)] = False 
            return dp[(i, j)]
    
        return recur(0, 0) 