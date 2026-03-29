# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # No Help solved myself in 23 minutes
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        temp1 = ListNode()
        temp1.next = prev
        temp2 = None
        if n == 1:
            newPrev = prev.next
            prev.next = None
            prev = newPrev
        while n != 0:
            temp2 = temp1
            temp1 = temp1.next
            n -= 1
        temp2.next = temp1.next
        temp1.next = None
        tail = None
        current = prev
        while current:
            temp = current.next
            current.next = tail
            tail = current
            current = temp
        return tail
        