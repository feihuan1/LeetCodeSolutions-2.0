// backtrack approach 
// count open and close 
// if open == close == n , its valid -> push to result 
// if open < n, can add open P 
// if close < open, can add a close P

// time: O(2^n)
// space: O(2^n)


var generateParenthesis = function(n) {
    // if no semi colon, it will add the parentheses after the array, witch will cuase type error result is not a function!!!
    // code interprets down below with no semi colon
    // const result = [](function backtrack() {
    //     result.push('2');
    // })();
    const result = [];// Immediately Invoked Function Expression wont work if missing this semi colon
    // 3 ways to create IIFE -> wrap in () then fire -> use a Unary operator ! -> use void

    // (function backtrack() {
    //     result.push('2');
    // })(); 

    // !function backtrack() {
    //     result.push('2');
    // }(); 

    void function backtrack(s='', openC = 0, closeC = 0,) {
        if(s.length === n * 2) {
            result.push(s) 
            return
        }

        if(openC < n) {
            backtrack(s + '(', openC+1, closeC)
        }

        if(closeC < openC) {
            backtrack(s+")", openC, closeC+1)
        }
    }(); 

    return result;
};



console.log(generateParenthesis(3)); // Output: ["2"]