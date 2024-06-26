// Given an integer x, return true if x is a palindrome , and false otherwise.

// if negative input, it's impossible for pal 
// use math revers number 
// return reversed = input


//time: O(log10(x)) -> O(log n) 
//space: O(1)

var isPalindrome = function(x) {
    if(x < 0) return false 

    let copy = x
    let pal = 0 

    while(copy > 0) {
        let tail = copy % 10 
        pal = pal * 10 + tail 
        copy = Math.floor(copy / 10)
    }

    return pal === x

};