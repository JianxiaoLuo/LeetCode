# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Add l1 and l2 bit by bit. The difficult part is that they may be in different length, and the carry bit should be considered.
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1 = l1
        c2 = l2
        carry = 0
        res = ListNode(0)
        curr = res
        while c1 or c2:
            x = c1.val if c1 else 0
            y = c2.val if c2 else 0
            v = carry + x + y
            carry = v//10
            curr.next = ListNode(val = v % 10)
            curr = curr.next
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
        if carry > 0:
            curr.next = ListNode(val = carry)
        return res.next
            
