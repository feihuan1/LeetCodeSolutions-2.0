# // difine a roman to interger obj key value pair , and iniitialize result to 0 

# // loop input string 
# // if next char in obj's balue is bigger, res plue obj next char - obj's current char, and skip next char buy i++ 
# // else just add obj's current char to res

# // **has to handle index out bounce with nextChar in python, 

# // time: O(n)
# // space: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0

        for index in range(len(s)):
            char = s[index] 
            next_char = s[index + 1] if index + 1 < len(s) else 'I'

            if dic[next_char] > dic[char]:
                res -= dic[char] 
            else:
                res += dic[char]
 
        return res