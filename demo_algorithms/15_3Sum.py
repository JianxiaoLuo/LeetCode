# My solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        res = []
        
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = i+1
            b = l-1
            while a < b:
                add = nums[i] + nums[a] + nums[b]
                if add == 0:
                    res_1 = [nums[i], nums[a], nums[b]]
                    res.append(res_1)
                    a += 1
                    b -= 1
                    while a < b and nums[a] == nums[a-1]:
                        a += 1
                    while a < b and nums[b] == nums[b+1]:
                        b -= 1
                if add < 0:
                    a += 1
                if add > 0:
                    b -= 1
                
        return res 
                    
