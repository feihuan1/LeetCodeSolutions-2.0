// handle out of bounce first 
// set operator if its positive 
// loop while dividend biger or equal divisor 
// set sum and count 
// while 2 sum small than dividend, doulble sum and count 
// when out of loop dividend subtract the sum and add count to res 
// return res depends on isPositive 

//Time: O(log n)
//Space: O(1)
var divide = function(dividend, divisor) {
    if (dividend === -2147483648 && divisor === -1) return 2147483647;
    let isPositive = (dividend >= 0 && divisor > 0) || (dividend <= 0 && divisor < 0)  

    dividend = Math.abs(dividend)
    divisor = Math.abs(divisor)

    let res = 0

    while (dividend >= divisor) { 
        let count = 1
        let multi = divisor 
        while(dividend >= multi + multi){
            multi += multi 
            count += count
        } 
        dividend -= multi 
        res += count

    }
    return isPositive? res : - res
};