# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.isKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            curr = groupPrev.next
            prev = groupNext
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp
        return dummy.next
                         
    def isKth(self, curr, k):
        while k > 0 and curr:
            curr = curr.next
            k -= 1
        return curr
        