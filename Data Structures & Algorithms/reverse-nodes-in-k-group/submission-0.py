class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1:45 Mins thought of all the logic myself but small details tripped me up the commented python code is mine and it pass 1 testcase and failed the other so used GPT since I was almost 90% there
        onepass = head
        length = 0
        while onepass:
            onepass = onepass.next
            length += 1

        groups = length // k
        if groups == 0:
            return head

        curr = head
        newhead = None      
        newtail = None     

        while groups:
            block_head = curr
            prev = None            
            count = k
            while count:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count -= 1
            if newhead is None:
                newhead = prev       
            if newtail is not None:
                newtail.next = prev 

            newtail = block_head     
            groups -= 1

        newtail.next = curr

        return newhead
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         onepass = head
#         length = 0
#         prev = None
#         curr = head
#         temp = None
#         temp2 = None
#         newhead = head
#         newtail = head
#         while onepass:
#             onepass = onepass.next
#             length += 1
#         groups = length // k
#         if (length % k) != 0:
#             groups = floor(groups)
#         else:
#             pass
#         unchangedgroup = groups
#         while groups:
#             count = k
#             if temp:
#                 newtail = temp
#             while count:
#                 temp = curr.next
#                 if temp2:
#                     temp = temp2
#                 else:
#                     pass
#                 if unchangedgroup == groups:
#                     newhead = curr
#                 curr.next = prev
#                 prev = curr
#                 curr = temp
#                 count -= 1
#             temp2 = temp
#             groups -= 1
#         if temp2:
#             newtail.next = temp2
#         return newhead
# Why your original reverseKGroup implementation failed
#
# 1) `prev` wasn’t reset per group
#    - You set prev = None once, outside the loop over groups.
#    - After reversing the first k-block, prev points to that block’s new head.
#    - The next block’s reversal starts with a “dirty” prev instead of None,
#      corrupting pointers during subsequent reversals.
#
# 2) The temp / temp2 interplay breaks the natural next-pointer flow
#    - Inside the inner loop you do:
#        temp = curr.next
#        if temp2: temp = temp2
#      After the first group, temp2 becomes a non-None pointer.
#      From then on, every iteration force-sets temp = temp2,
#      ignoring curr.next and “jumping” to a stale pointer.
#    - This can skip nodes or collapse the tail reference, causing truncation.
#
# 3) `newtail` is mis-tracked
#    - You set `newtail = temp` before finishing the group reversal.
#    - But `temp` is just a moving “next” pointer while reversing; it is not
#      the true tail of the processed portion.
#    - The correct tail after reversing a block is the original block head
#      (the node where the block started before reversal).
#
# 4) Wrong moment to set the new list head for the first group
#    - You do `if unchangedgroup == groups: newhead = curr` during the inner loop.
#    - While reversing, `curr` is advancing; it does not represent the final
#      head of the reversed block.
#    - The true new head of a reversed k-block is the node held in `prev`
#      after the k iterations complete (the kth node of the block).
#
# 5) Missing stitching between consecutive reversed blocks
#    - After each k-block is reversed, you must connect the previous block’s tail
#      to the current block’s new head (prev at end of reversal).
#    - Your code only attempts a single final stitch at the end:
#        if temp2: newtail.next = temp2
#      That attaches only the leftover (remainder) once, not the boundaries
#      between k-blocks. As a result, blocks aren’t chained together.
#
# 6) Unnecessary math adds confusion
#    - `groups = length // k` already floors; the extra floor() check
#      is redundant and distracts from pointer logic.
#
# Consequence on the failing test: head = [1,2,3,4,5], k = 2
# - The first k-block (1,2) reverses to 2->1.
# - Because temp2 begins to override temp and newtail is not the true tail,
#   the pointer from the end of the reversed block (node 1) to the remainder
#   (node 3) is never properly set.
# - The list gets truncated after the first block, yielding [2,1] instead of
#   correctly attaching 3->4->5 to produce [2,1,4,3,5].
#
# Key fixes conceptually (without rewriting your code here):
# - Reset `prev = None` at the start of each k-block reversal.
# - Track `block_head = current_start` so you can use it as the new tail
#   after reversal.
# - After reversing k nodes, connect (previous_tail).next -> (new_block_head)
#   and set previous_tail = block_head.
# - Don’t override `temp` with `temp2` inside the loop; rely on `curr.next`.
# - After processing all full groups, attach the leftover: previous_tail.next = curr.
