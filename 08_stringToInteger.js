/**
 * @param {string} s
 * @return {number}
 */

// res = 0 operator = 1 by default, i = 0
 // read and ignore leading white space 
 // loop s and check leading whitespace 
// check next char is + or - 
// while next char is numeric, add to res 
// handle out of bounce res 
// return res * operator, (0 if no number read two step above) 

//time: O(n) 
//space: O(1)

var myAtoi = function(s) {
    let i = 0;
    let operator = 1;
    let res = 0;

    const min = -(2**31) 
    const max = (2 ** 31) - 1

    while(i < s.length && s[i] === ' '){
        i++
    }

    if(i < s.length && (s[i] === "-" || s[i] === "+") ) {
        operator = s[i] === "-" ? -1 : 1
        i++
    } 

    while(i < s.length && s[i] >= '0' && s[i] <= '9') {
        let num = s[i] - 0
        res = res * 10 + num 
        i++
    }

    res *= operator

    if(res < min) return min 
    if(res > max) return max

    return res
};
