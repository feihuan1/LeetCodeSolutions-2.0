# // difine a roman to interger obj key value pair , and iniitialize result to 0 

# // loop input string 
# // if next char in obj's balue is bigger, res plue obj next char - obj's current char, and skip next char buy i++ 
# // else just add obj's current char to res

# // handle the last char in s

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

        for index in range(len(s)-1):
            char = s[index] 
            next_char = s[index + 1]

            if dic[next_char] > dic[char]:
                res -= dic[char] 
            else:
                res += dic[char]
        res += dic[s[-1]]
        return res