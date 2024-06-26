# // if negative input, it's impossible for pal 
# // use math revers number 
# // return reversed = input


# //time: O(log10(x)) -> O(log n) 
# //space: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False 

        copy = x 
        pal = 0 

        while copy > 0: 
            tail = copy % 10 
            pal = pal * 10 + tail 
            copy = copy // 10 

        return pal == x