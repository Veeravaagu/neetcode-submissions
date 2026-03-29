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
        #did not think of hashmap decided to use variables to store val next and random create node and assign them but i knew it would only be a reference so i looked at neetcode solution hints saw hash usage. Couldn't get the syntax down so used GPT.
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


        