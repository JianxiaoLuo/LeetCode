class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        
        while l <= h:
            # Search from the left end and right end, and move to the center
            m = l + (h-l) // 2
            
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
            else:
                h = m-1
        
        return l
