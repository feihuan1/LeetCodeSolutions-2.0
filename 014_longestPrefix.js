// # brute force solution

// # find shortest word in array, and initialize res = '' 
// # loop the shortest and loop the array inside, if each words in array dont match the shortest at i, return res, 
// # if matchs , ass the letter into res 

// #time: O(n*m) 
// #space: O(1)
var longestCommonPrefix = function(strs) {
    if(strs.length === 0) return ''
    let res = '' 
    let shortest = '' 
    for(let i = 0; i< strs.length; i++) {
        if(strs[i].length > shortest.length) {
            shortest = strs[i]
        }
    }

    for(let j = 0; j < shortest.length; j++) {
        for(let word of strs){
            if(word[j] !== shortest[j]) {
                return res
            }
        }
        res += shortest[j]
    }
    return res
};

// binary search 

//define helper func take in end index and find out if substring end with it can prefix all element is strs array
// use strs[0] and slice with 0 and end as prefix test case, loop strs arr and see if every element startsWith() prefix 

// find out shortest element length in strs arr 
// set two pointer 0 and shortest lenth element and run binary search 
// while l <= r, find mid, run isMatch help func pass in mid, if true, move l forward, if false , move r backwars
// return strs[0] slice at 0 and final average of l and r(floor)

// #time: O(n) 
// #space: O(1)
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return ''

    const isMatch = (end) => {
        let prefix = strs[0].substring(0, end) 

        for(let i = 0; i < strs.length; i++) {
            if(!strs[i].startsWith(prefix)) {
                return false
            }
        }
        return true
    }

    let minLen = strs[0].length 

    for(let i = 0; i < strs.length; i++) {
        minLen = Math.min(minLen, strs[i].length )
    }

    let l = 0 
    let r = minLen 

    while( l <= r) {
        const mid = Math.floor((l + r) / 2) 

        if(isMatch(mid)) {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }

    const finalMid = Math.floor((l + r) / 2)
    return strs[0].substring(0, finalMid)
}