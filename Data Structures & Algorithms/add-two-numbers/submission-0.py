# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum =  x + y + carry
            digit = sum % 10
            carry = sum // 10

            temp.next = ListNode(digit)
            temp = temp.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return result.next
        # fix(add-two-numbers): issues that caused crashes/wrong results
#
# 1) Loop condition:
#    - Used `while l1 or l2 is not None:` → parses as `(l1) or (l2 is not None)`,
#      so you still entered with l1=None and then did l1.val → AttributeError.
#    - Then switched to `while l1 is not None and l2 is not None:` which stops
#      as soon as one list ends; you must continue if either list has nodes or there’s a carry.
#
# 2) Dereferencing None:
#    - Computed `l1.val + l2.val` unconditionally; if either is None (lists of unequal length),
#      this crashes. You need to treat missing nodes as 0.
#
# 3) No explicit carry:
#    - Tried to encode carry with `sum/new` branches (e.g., `new = sum - 10`, later `sum + 1`);
#      this adds +1 even when no carry and misses the final carry at the end (e.g., 999 + 1).
#      Carry must be tracked separately per step and appended at the end if nonzero.
#
# 4) Wrong digit appended:
#    - Appended `sum` or `sum - 10` directly instead of the ones digit (`total % 10`).
#      The tens place should become the carry (`total // 10`), not be added into the node value.
#
# 5) Shadowing built-in:
#    - Used variable name `sum`, shadowing Python’s built-in `sum()` function.
#
# 6) Result pointer usage:
#    - Earlier version recreated `result = ListNode()` inside the loop and returned `result`,
#      which would discard the built list. Correct is to use a sentinel `result` once,
#      build via `temp = result`, and finally `return result.next`.
#
# 7) Edge cases unhandled:
#    - Different lengths (e.g., [2,4,3] + [5,6]) and long carry chains (e.g., [9,9,9] + [1])
#      failed due to the issues above.
#
# Takeaway:
# - Loop while (l1 or l2 or carry), treat missing nodes as 0, compute digit = (x+y+carry)%10,
#   update carry = (x+y+carry)//10, link new digit node via a tail pointer, return sentinel.next.