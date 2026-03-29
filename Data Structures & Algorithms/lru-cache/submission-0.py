class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

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

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# fix(lru-cache): issues summary + snapshot of my code at this point
#
# What went wrong in my LRU attempts:
# - No dict<->list integration: I didn’t consistently keep key -> node in a map
#   AND maintain order in a doubly linked list for O(1) moves.
# - Singly vs doubly: LRU needs prev/next to unlink in O(1); early versions used only next.
# - Capacity misuse: treated capacity as a counter to consume; should keep a fixed cap and evict when size > cap.
# - get(): returned raw dict value, didn’t move the node to MRU; also sometimes inserted None on miss.
# - put(): didn’t handle “update existing key”; didn’t evict LRU when full.
# - List ops: created/rotated locals (dummy/head/temp) that weren’t persisted on self; risked None derefs.
# - Name/logic pitfalls: used undefined names (val vs value), shadowed builtins, and forgot to sync dict and list.
#
# Required LRU behavior (for future me):
# - Dict: key -> node (node holds key, val, prev, next)
# - Doubly linked list with sentinels: head.next = LRU, tail.prev = MRU
# - get(k): if miss -> -1; if hit -> move node to MRU, return val
# - put(k, v): if exists -> update + move to MRU; else append node as MRU; if size > cap -> evict LRU + del from dict
#
# ---- Snapshot of my code at this moment (kept for history) ----
# class LRUCache:
#     class Node:
#         def __init__(self, key, val, next = None, prev = None):
#             self.val = val
#             self.key = key
#             self.next = next
#             self.prev = prev
#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.size = capacity
#         self.count = 0
#         self.dummy = self.Node(0, 0)
#         self.tail = self.dummy
#     def get(self, key: int) -> int:
#         node = self.cache.get(key)
#         return -1 if node is None else node.val
#
#     def put(self, key: int, value: int) -> None:
#         if self.count < self.size:
#             newnode = self.Node(key, value)
#             self.cache[key] = newnode
#             self.tail.next = newnode
#             newnode.prev = self.tail
#             self.tail = newnode
#             self.count += 1
#         head = self.dummy.next
#         if head is not None:
#             temp = head.next
#             self.dummy.next = temp
#             if temp:
#                 temp.prev = self.dummy
#             head.next = None
#             head.prev = self.tail
#             self.tail.next = head
#             self.tail = head
# fix(lru-cache): why earlier attempts failed (issues summary)
#
# Core design mistakes
# - No dict <-> list integration: never kept a map of key -> node (so get/put couldn’t find/move nodes in O(1)).
# - Used a singly linked list; LRU needs a DOUBLY linked list (prev/next) to unlink in O(1).
# - Built local chains inside put (fresh dummy/tail each call) that were discarded; no persistent head/tail on self.
# - Treated capacity as a consumable counter (while self.size / self.size -= 1) instead of a fixed cap + current size.
#
# API-specific mistakes
# - get(): returned raw dict value or mutated dict with defaults; didn’t move the node to MRU (tail) on hit.
# - put(): ignored “update existing key” path (should update value + move to MRU); never evicted when full.
# - put(): appended nodes but didn’t add to dict or remove from dict on eviction; linked list and dict got out of sync.
#
# Linked-list handling mistakes
# - No sentinels (head/tail) → lots of edge cases; moving “head to tail” unconditionally corrupted order.
# - Didn’t guard None when touching head.next; risked AttributeError on empty list.
# - Forgot to update BOTH neighbors when unlinking/linking (need prev/next assignments on both sides).
#
# Dict usage mistakes
# - Key errors / NameErrors: used cache[key] after get() without checking, or referenced undefined 'cache' var.
# - Truthiness checks: treating 0 as missing (if self.cache[key]: …); must check membership, not truthiness.
# - Overwrote entries on miss: self.cache[key] = self.cache.get(key) inserts None for absent keys.
#
# Runtime/syntax pitfalls seen
# - Missing method bodies (put without body), wrong constructor calls (self.Node() without required args),
#   undefined variables (val vs value, size vs self.size, Node vs self.Node), and unused locals (head/temp).
#
# Required LRU behavior (for future reference)
# - Dict: key -> node
# - Doubly linked list with sentinels: head.next is LRU, tail.prev is MRU
# - get(key):
#     * if miss -> -1
#     * if hit  -> move node to MRU; return node.val
# - put(key, value):
#     * if key exists -> update val, move to MRU
#     * else -> append new node as MRU, add to dict; if size > capacity, evict LRU (head.next) and del from dict
#
# Quick checklist before submitting
# [ ] Node has key, val, prev, next
# [ ] _remove(node) and _append_to_tail(node) helpers are correct
# [ ] get() moves hit to MRU
# [ ] put() handles update vs insert; evicts when over cap
# [ ] Dict and list always updated together (no stale entries)
# [ ] No NameErrors / KeyErrors / None derefs
