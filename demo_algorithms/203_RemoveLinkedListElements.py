# My solution
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = head
        # Check if it is a null list
        if not head:
            return head
       
        while head.next:
            if head.next.val == val:
                if head.next.next:
                    head.next.val = head.next.next.val
                    head.next = head.next.next
                else:
                    head.next = None
            else:
                head = head.next
                
        # Check the final node
        if res.val == val: 
            if res.next:
                res.val = res.next.val
                res.next = res.next.next
            else: res = None
        return res
        

# Second version
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        front = ListNode(None)
        
        # Set a pointer points to the former position
        front.next = head
        start = front
        while start.next:
            if start.next.val == val:
                start.next = start.next.next
                # print(head.val)
            else:
                start = start.next
        return front.next
