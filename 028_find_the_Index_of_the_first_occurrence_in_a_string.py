# loop haystack if char match first char of needle, run match function, return the index if perfect match, if out of loop, no match return -1
# time: O(n*m)
# space: O(1)
#!!!! there is a better solution: Knuth-Morris-Pratt (KMP) algorithm make time O(n+m)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if self.perfect_match(haystack, needle, i):
                    return i 
        return -1

    def perfect_match(self, h, n, start): 
        for i in range(len(n)): 
            if h[start] != n[i]:
                return False 
            else:
                start+=1 
        return True