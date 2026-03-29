# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            newValue = total if total < 10 else total - 10
            head.next = ListNode(newValue)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            if l1:
                total = l1.val + carry
                carry = total // 10
                newValue = total if total < 10 else total - 10
                head.next = ListNode(newValue)
                head = head.next
                l1 = l1.next
            if l2:
                total = l2.val + carry
                carry = total // 10
                newValue = total if total < 10 else total - 10
                head.next = ListNode(newValue)
                head = head.next
                l2 = l2.next
        if carry != 0:
            head.next = ListNode(1, None)
        return dummy.next


        