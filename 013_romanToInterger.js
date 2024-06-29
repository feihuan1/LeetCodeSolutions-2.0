// difine a roman to interger obj key value pair , and iniitialize result to 0 

// loop input string 
// if next char in obj's balue is bigger, res plue obj next char - obj's current char, and skip next char buy i++ 
// else just add obj's current char to res

// time: O(n)
// space: O(1)

var romanToInt = function(s) {
    const obj = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };

    let res = 0 

    for(let i = 0; i < s.length; i++) {
        const char = s[i] 
        const nextChar = s[i+1] 
        if(obj[nextChar] > obj[char]){
            res += (obj[nextChar] - obj[char]) 
            i++
        } else {
            res += obj[char]
        }
    }

    return res

};