# // Given a string s, find the length of the longest substring without repeating characters.

# // time: O(n)
# // spcae: O(min(n, m))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1.use a set to store existing chars of substring 
        # 2.initialize i, j two pointer to check substring , set res to be 0 and update later
        # 3.loop input string while i, j both smaller than lenth of s;
        # 4.if s[j] not in set, means no duplicates,add s[j] in set and increment j to try next char, update res tobe max(res, j - i)
        # 5.else means duplicate found, remove s[i], and increment i to try again

        char_set = set() 
        i, j, res = 0, 0, 0 

        while i < len(s) and j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1 
                res = max(res, j - i)
            else:
                char_set.remove(s[i]) 
                i += 1

        return res