# // back track approach 
# // define res as arr and hard code digit to letter map, handle digits=[] edge case 
# // define backtrack function and run it at (0, '')

# // backrack function:
# // base case is when curStr we are building equals input digit length 
# // find the index of i in obj, 
# // loop through it and run backTrack recursively at (i+1, letters[loop_index])


# //time: O(4^n) 
# //space: (n * 4^n)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0: return []

        obj = {
        "2" : 'abc',
        "3" : 'def',
        "4" : 'ghi',
        "5" : 'jkl',
        "6" : 'mno',
        "7" : 'pqrs',
        "8" : 'tuv',
        "9" : 'wxyz',
        }
        res = []

        def backTrack(i, cur_str): 
            if len(cur_str) == len(digits): 
                res.append(cur_str) 
                return 
            
            for c in obj[digits[i]]:
                backTrack(i+1, cur_str + c)

        backTrack(0,'')

        return res

        