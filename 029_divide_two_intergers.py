# // handle out of bounce first 
# // set operator if its positive 
# // loop while dividend biger or equal divisor 
# // set sum and count 
# // while 2 sum small than dividend, doulble sum and count 
# // when out of loop dividend subtract the sum and add count to res 
# // return res depends on isPositive 

# //Time: O(log n)
# //Space: O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1: 
            return 2147483647 
        positive = (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor) 

        res = 0

        while dividend >= divisor:
            count = 1 
            sum = divisor 
            while dividend >= sum + sum : 
                sum += sum 
                count += count 
            dividend -= sum 
            res += count
        return res if positive else -res