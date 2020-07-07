# my solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        carry = 1
        
        # Loop backwards
        for i in range(l-1, -1, -1):
            num = digits[i] + carry
            digits[i] = num % 10
            carry = num // 10
        
        if carry != 0:
            return [1] + digits
        else:
            return digits
            
            
# Sample 20ms solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        for idx, x in enumerate(digits[::-1]):
            num += (x*10**idx)
        return list(str(num))
