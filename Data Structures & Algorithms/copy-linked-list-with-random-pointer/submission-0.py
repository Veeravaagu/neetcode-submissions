"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            clone = hashmap[curr]
            clone.next = hashmap.get(curr.next)
            clone.random = hashmap.get(curr.random)
            curr = curr.next
        return hashmap.get(head)


        