# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        count = 0
        while fast and fast.next:
            count += 1
            slow = slow.next
            fast = fast.next.next
        #Even Length
        if not fast:
            length = count * 2
        #Odd
        else:
            length = (count * 2) + 1
        if n == length:
            return head.next
        pos = length - n
        slow = head
        count = 0
        while count + 1 < pos:
            slow = slow.next
            count += 1
        slow.next = slow.next.next
        return head


