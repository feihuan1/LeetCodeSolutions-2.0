// # loop haystack if char match first char of needle, run match function, return the index if perfect match, if out of loop, no match return -1

// # time: O(n*m)
// # space: O(1)
// #!!!! there is a better solution: Knuth-Morris-Pratt (KMP) algorithm make time O(n+m)

public class Solution {
    public int StrStr(string haystack, string needle) {
        if (needle.Length == 0) return 0;
        
        for (int i = 0; i <= haystack.Length - needle.Length; i++) {
            if (haystack[i] == needle[0]) {
                int j;
                for (j = 0; j < needle.Length; j++) {
                    if (haystack[i + j] != needle[j]) {
                        break;
                    }
                }
                if (j == needle.Length) {
                    return i;
                }
            }
        }

        return -1;
    }
}