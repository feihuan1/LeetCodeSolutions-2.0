// # use dynamic programing
// # define dp dictionary

// # make recursive func
// # 3 base case: if (i,j) in dp, return it , if both str out of bounce(has to be >=len()), it true, if p out of bounce, it's false for sure, (i out of bounce might be true because p end with char + * could be None)
// # define match, i must in bounce , si = pj or pj = .!!
// # check if next char of Pj is a *, (next cahr of pj has to in bounce)
// # if it is, set cache of (i,j) to be recur(i, j+ 2)[dont use *] or (match[if use *, first char has to be the same] and recur(i + 1, p)[use *]) -> return cache at (i, j)
// # if not *, check if match, set cache[(i,j)] to be move both pointer forward
// # if nothing happen, cache[(i,j)] = false and return false

// # just return dp(0,0)

// # time: O(n * m)
// # space: O(n * m)

var isMatch = function (s, p) {
  const dp = {};

  const recur = (i, j) => {
    let key = `${i}-${j}`
    // base case
    if (key in dp) return dp[key]; //or if(dp.hasOwnProperty(key)){...}
    if (i >= s.length && j >= p.length) return true;
    if (j >= p.length) return false;

    const match = i < s.length && (s[i] === p[j] || p[j] === '.') 

    if(j + 1 < p.length && p[j+1] === '*') {
        //                   not use *       use *
        dp[key] = recur(i, j+2) || (match && recur(i+1, j)) 
        return dp[key]
    }

    if(match){
        dp[key] = recur(i+1, j+1) 
        return dp[key]
    }

    dp[key] = false 
    return dp[key]
  };

  return recur(0,0);
};

console.log(isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"));
