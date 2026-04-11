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
        pointer = head
        hashmap = {}
        while pointer:
            hashmap[pointer] = Node(pointer.val)
            pointer = pointer.next
        pointer = head
        while pointer:
            hashmap[pointer].next = hashmap.get(pointer.next)
            hashmap[pointer].random = hashmap.get(pointer.random)
            pointer = pointer.next
        return hashmap.get(head)