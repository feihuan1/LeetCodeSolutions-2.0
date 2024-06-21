// Given a string s, find the length of the longest substring without repeating characters.

// time: O(n)
// spcae: O(min(n, m))

var lengthOfLongestSubstring = function(s) {
    // # 1.use a set to store existing chars of substring 
    // # 2.initialize i, j two pointer to check substring , set res to be 0 and update later
    // # 3.loop input string while i, j both smaller than lenth of s;
    // # 4.if s[j] not in set, means no duplicates,add s[j] in set and increment j to try next char, update res tobe max(res, j - i)
    // # 5.else means duplicate found, remove s[i], and increment i to try again

    const charSet = new Set() 
    let i = 0 
    let j = 0
    let res = 0 

    while(i < s.length && j < s.length) {
        if(!charSet.has(s[j])) {
            charSet.add(s[j]) 
            j ++ 
            res = Math.max(res, j - i)
        } else {
            charSet.delete(s[i]) 
            i++
        }
    }

    return res
};