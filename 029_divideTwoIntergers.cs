// handle out of bounce first 
// set operator if its positive 
// loop while dividend biger or equal divisor 
// set sum and count 
// while 2 sum small than dividend, doulble sum and count 
// when out of loop dividend subtract the sum and add count to res 
// return res depends on isPositive 

//Time: O(log n)
//Space: O(1)

public class Solution {
    public int Divide(int dividend, int divisor) {
        if (dividend == int.MinValue && divisor == -1) return int.MaxValue;

        bool isPositive = (dividend >= 0 && divisor > 0) || (dividend <= 0 && divisor < 0);

        long absDividend = Math.Abs((long)dividend);
        long absDivisor = Math.Abs((long)divisor);

        int result = 0;

        while (absDividend >= absDivisor) {
            long multi = absDivisor;
            int count = 1;
            while (absDividend >= (multi + multi)) {
                multi += multi;
                count += count;
            }
            absDividend -= multi;
            result += count;
        }

        return isPositive ? result : -result;
    }
}