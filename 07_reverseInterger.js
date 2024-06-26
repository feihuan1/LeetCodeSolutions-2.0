// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// set operator to be 1 or -1 depends on input 
// get abs value of input 
// set res and loop until abs value is not 0 
//res * 10 add abs % 10 then devide abs by 10 floor it 
// handle out bounce case when exit loop 
// return res * operator 


// time: O(log n)
// space: O(1)

var reverse = function(x) {
    let operator = 1 
    if( x < 0) operator = -1 

    let absInput = Math.abs(x) 

    let res = 0 

    while (absInput > 0) {
        let tail = absInput % 10 
        res = res * 10 + tail 
        absInput = Math.floor(absInput / 10) 
        console.log(res, absInput)
    }

    if(res < -(2 ** 31) || res > (2 ** 31) -1) return 0

    return res * operator

};