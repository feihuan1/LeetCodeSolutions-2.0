// back track approach 
// define res as arr and hard code digit to letter map, handle digits=[] edge case 
// define backtrack function and run it at (0, '')

// backrack function:
// base case is when curStr we are building equals input digit length 
// find the index of i in obj, 
// loop through it and run backTrack recursively at (i+1, letters[loop_index])


//time: O(4^n) 
//space: (n * 4^n)

var letterCombinations = function(digits) {
    if (digits.length === 0) return []
    const obj = {
        2 : 'abc',
        3 : 'def',
        4 : 'ghi',
        5 : 'jkl',
        6 : 'mno',
        7 : 'pqrs',
        8 : 'tuv',
        9 : 'wxyz',
    } 

    const res = [] 

    function backTrack(i, curStr){
        if(curStr.length === digits.length) {
            res.push(curStr) 
            return
        }

        const letters = obj[digits[i]] 

        for ( let c of letters) {
            backTrack(i + 1, curStr + c)
        }

    }
    
    backTrack(0, '')
    return res
}
