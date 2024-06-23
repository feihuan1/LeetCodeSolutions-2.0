# Given a string s, return the longest palindromic substring in s.

class Solution:
    # initialize res as return output "" 
    # loop through chars in s , set l and r pointer at i in odd case, l = i, r = i+ 1 in even case
    # for every char, treat as middle of palindrom, mid i and mid i -> i + 1, for both odd and even case 
    # in both case, while l and r in bound and equal to each other, it is still palindrome 
    # if curent substring longer than res, set res to curent substring, and decrement i also increament r 
    # keep doing it until it's not palindrom
    # return res


    # Manacher's algorithm
    # time O(n^2) -> best solution I can think of so far, keep improving 
    # space O(1)

    
    def longestPalindrome(self, s: str) -> str:
        res = '' 

        for i in range(len(s)): 
             l, r = i, i 
             while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l: r + 1] 
                l -= 1 
                r += 1 

             l, r = i, i+1 
             while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l: r + 1] 
                l -= 1
                r += 1
        return res