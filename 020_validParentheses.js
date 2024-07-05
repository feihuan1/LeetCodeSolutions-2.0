// # define parentheses object and stack array 
// # loop s, if in object-> means it's open bracket, push closing in to stack 
// # else if its closing bracket, it has to equal the top of stack (make sure stack is not empty before pop) , else return false
// # return true if stack empty at end of loop


// # time: O(n)
// # space: O(n)

var isValid = function(s) {
    const obj = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    const stack = [] 

    for(let i = 0; i < s.length; i++) {
        if (obj.hasOwnProperty(s[i])) {
            stack.push(obj[s[i]])
        } else {
            if (stack.length === 0 || s[i] !== stack.pop()) {
                return false
            }
        }
    }
    return stack.length === 0
};