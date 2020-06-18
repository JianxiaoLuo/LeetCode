# My solution, using linear searching, O(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        for i in range(l):
            if citations[i] >= (l-i):
                return l-i
        return 0
        

# Better solution, binary searching, O(log n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            idx = (l + r)//2
            if n - idx - 1 < citations[idx]:
                r = idx
            else:
                l = idx + 1
        return n - l
