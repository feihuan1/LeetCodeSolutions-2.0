// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

 // if s.length  = 1 or length < numRows, return s 
 // initial res and indexJump( numRows * 2 - 2 ) 
 // loop numRows 
 // set i = row midIndexJump (if not first and last row, need add the mid char)
 // midIndexJump = indexJump - 2 * currentRow (v shape; row starts 0 so - 2)
 // while i < s.length, res add s[i] and if its not first or last row and the  i + midindex is in bounce, means there is a mid char, add that cahr s[i + midIndexJump]

 // time: O(n) 
 // space O(n)
 var convert = function(s, numRows) {
    if (s.length === 1 || s.length <= numRows) return s

    let res = '' 
    let indexJump = (numRows - 1) * 2

    for(let row = 0; row < numRows; row ++) {
        
        let i = row; 
        let midIndexJump = indexJump - 2 * row
        while(i < s.length) {
            res += s[i] 
            if(row > 0 && row < numRows - 1 && i + midIndexJump < s.length) {
                res += s[i + midIndexJump]
            }
            i += indexJump 
        }
    }
    return res
};