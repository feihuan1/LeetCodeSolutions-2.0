// # loop haystack if char match first char of needle, run match function, return the index if perfect match, if out of loop, no match return -1

// # time: O(n*m)
// # space: O(1)
// #!!!! there is a better solution: Knuth-Morris-Pratt (KMP) algorithm make time O(n+m)

var strStr = function (haystack, needle) {
    outerLoop: 
    for (let i = 0; i < haystack.length - needle.length + 1; i++) {
      if(haystack[i] === needle[0]){
        for (let j = 0; j < needle.length; j++) {
          if (haystack[i + j] !== needle[j]) {
            continue outerLoop;
          }
        }
        return i;
      }
    }
    return -1;
  };
  