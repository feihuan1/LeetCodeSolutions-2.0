
# define parentheses object and stack array 
# loop s, if in object-> means it's open bracket, push closing in to stack 
# else if its closing bracket, it has to equal the top of stack (make sure stack is not empty before pop) , else return false
# return true if stack empty at end of loop


# time: O(n)
# space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }

        stack = [] 

        for char in s:
            if char in p_map:
                stack.append(p_map[char])
            else:
                if not stack or char != stack.pop():
                    return False 
        
        return not stack