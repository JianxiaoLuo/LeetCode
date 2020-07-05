# My Solution %18  (bad)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Transform to binary string
        s1 = "{0:b}".format(x)
        s2 = "{0:b}".format(y)
        
        l1 = len(s1)
        l2 = len(s2)
        
        # Add '0' infront of short string, to make them the same length
        if l1 > l2:
            s2 = '0' * (l1 - l2) + s2
        else:
            s1 = '0' * (l2 - l1) + s1
        
        # Count the different bits
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        
        return count


# Better solution (without using bit manipulation) 92%
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x > 0 or y > 0:
            res = res + (0 if (x % 2 == y % 2) else 1)
            x = x // 2
            y = y // 2
        return res
        
 
# Using bit manipulation 8% (much slower, but with shorter code)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        output = x^y # XOR
        output = bin(output)         #.replace("0b","")
        return output.count('1') 

