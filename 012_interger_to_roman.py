
# insert 900, 400,90,40,5 into romanSymble list 
# loop throught and do the math

#time: O(1)
#space: O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        li = [
            ['M', 1000],
            ['CM', 900],
            ['D', 500],
            ['CD', 400],
            ['C', 100],
            ['XC', 90],
            ['L', 50],
            ['XL', 40],
            ['X', 10],
            ['IX', 9],
            ['V', 5],
            ['IV', 4],
            ['I', 1]
        ] 
        res = ''

        for sym, val in li:
            count = num // val 
            res += sym * count 
            num = num % val
        
        return res
