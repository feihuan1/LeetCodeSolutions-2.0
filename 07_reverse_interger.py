# // Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# // set operator to be 1 or -1 depends on input 
# // get abs value of input 
# // set res and loop until abs value is not 0 
# //res * 10 add abs % 10 then devide abs by 10 floor it 
# // handle out bounce case when exit loop 
# // return res * operator 


# // time: O(log n)
# // space: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        operator =  1 if x >= 0 else -1 
        abs_input = abs(x) 
        res = 0 

        while abs_input > 0:
            tail = abs_input % 10 
            res = res * 10 + tail 
            abs_input = abs_input // 10 

        if res < -(2 ** 31) or res > (2 **31) -1: 
            return 0 
        
        return res * operator