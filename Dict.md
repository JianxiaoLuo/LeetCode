## 1. Two Sum
- The complexity of `List.index()` is `O(n)`
- Using dict to store the mapping of item to its index can save running time by only iterate the list once

My solution:
```class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        dic = {}
        for i in range(l):
            if target - nums[i] in dic:
                return [i, dic[target-nums[i]]]
            else: dic[nums[i]] = i
```
