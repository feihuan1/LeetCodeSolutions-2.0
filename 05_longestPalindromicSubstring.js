// # Given a string s, return the longest palindromic substring in s.

var longestPalindrome = function(s) {
    // # initialize res as return output "" 
    // # loop through chars in s , set l and r pointer at i in odd case, l = i, r = i+ 1 in even case
    // # for every char, treat as middle of palindrom, mid i and mid i -> i + 1, for both odd and even case 
    // # in both case, while l and r in bound and equal to each other, it is still palindrome 
    // # if curent substring longer than res, set res to curent substring, and decrement i also increament r 
    // # keep doing it until it's not palindrom
    // # return res

    //Manacher's algorithm
    // # time O(n^2) -> best solution I can think of so far, keep improving 
    // # space O(1)

    let res = '' 

    for(let i = 0; i < s.length; i++) {
        let oddL = i
        let oddR = i 

        while(oddL >= 0 && oddR < s.length && s[oddL] === s[oddR]) {
            let sub = s.substring(oddL, oddR + 1) 
            if(sub.length > res.length) {
                res = sub
            } 
            oddL -- 
            oddR ++
        } 

        let evenL = i
        let evenR = i + 1

        while(evenL >= 0 && evenR < s.length && s[evenL] === s[evenR]) {
            let sub = s.substring(evenL, evenR + 1) 
            if(sub.length > res.length) {
                res = sub
            } 
            evenL -- 
            evenR ++
        } 

    }

    return res
};