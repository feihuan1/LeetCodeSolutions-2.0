
# brute force solution

# find shortest word in array, and initialize res = '' 
# loop the shortest and loop the array inside, if each words in array dont match the shortest at i, return res, 
# if matchs , ass the letter into res 

#time: O(n*m) 
#space: O(1)
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = '' 

        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]: 
                    return res 
            res += shortest[i]
                

        return res


# // binary search 

# //define helper func take in end index and find out if substring end with it can prefix all element is strs array
# // use strs[0] and slice with 0 and end as prefix test case, loop strs arr and see if every element startsWith() prefix 

# // find out shortest element length in strs arr 
# // set two pointer 0 and shortest lenth element and run binary search 
# // while l <= r, find mid, run isMatch help func pass in mid, if true, move l forward, if false , move r backwars
# // return strs[0] slice at 0 and final average of l and r(floor)

# // time: O(n) 
# // space: O(1) 

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str: 
        if len(strs) == 0: return '' 

        def is_match(end): 
            prefix = strs[0][:end] 
            for i in range(len(strs)):
                if not strs[i].startswith(prefix): 
                    return False 
            return True 
        
        min_len = len(min(strs, key=len)) 

        l = 0 
        r = min_len

        while l <= r:
            mid = (l + r) // 2 

            if is_match(mid):
                l = mid + 1 
            else:
                r = mid - 1

        final_mid = (l + r) // 2 

        return strs[0][:final_mid]
