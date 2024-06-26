
#  // res = 0 operator = 1 by default, i = 0
#  // read and ignore leading white space 
#  // use while loop s and check leading whitespace 
# // check next char is + or - 
# // while next char is numeric, add to res 
# // handle out of bounce res 
# // return res * operator, (0 if no number read two step above) 

# //time: O(n) 
# //space: O(1)


class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0 
        operator = 1 

        small = -(2 ** 31) 
        large = (2 ** 31) - 1
        
        i = 0 
        while i < len(s) and s[i] == ' ':
            i += 1
        

        if i < len(s) and (s[i] == "+" or s[i] == '-'):
            operator = 1 if s[i] == "+" else -1
            i += 1

        while i< len(s) and s[i].isnumeric(): 
            res = res * 10 + int(s[i]) 
            i += 1 

        res *= operator 

        if res < small: return small
        if res > large: return large

        return res
        
