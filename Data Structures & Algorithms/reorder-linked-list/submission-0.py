# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
                # couldn't think of reversing the second half but got the major outline like fast slow and two pointers from end to beginning, since thinking the tail cant decrement to prev thought of using fast and slow pattern:
        # input = 0 1 2 3 4 5 6
        # slow = 3 and fast = 6
        # swap them 0 -> 6; 5(tail.prev) -> 3
        # ignore the changed lists so 1 2 4 5 
        # do fast = 5 slow = 4 swap 1 -> 5 and 2 -> 4 so, 0 6 1 5 2 4 3
        # wrong logic but correct pattern recognition.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        