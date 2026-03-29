# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        length = 0
        while pointer:
            length += 1
            pointer = pointer.next
        pos = length - n
        prev = head
        if n == length:
            return head.next
        for _ in range(pos - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head





        