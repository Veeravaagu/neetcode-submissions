class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    def insert(self, node):
        temp1 = self.right.prev
        temp1.next = node
        node.prev = temp1
        node.next = self.right
        self.right.prev = node
        
    def remove(self, node):
        temp1 = node.next
        temp2 = node.prev
        temp2.next = temp1
        temp2.prev = temp1

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        lru = self.left.next
        if len(self.cache) > self.cap:
            self.remove(lru)
            del self.cache[lru.key]
            
            
            
