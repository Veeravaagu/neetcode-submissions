class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        countn = [0]*26
        countm = [0]*26

        for i in range(n):
            countn[ord(s1[i]) - ord("a")] += 1
            countm[ord(s2[i]) - ord("a")] += 1

        if countn == countm:
            return True

        for i in range(n, m):
            countm[ord(s2[i]) - ord("a")] += 1
            countm[ord(s2[i - n]) - ord("a")] -=1
            if countn == countm:
                return True

        return False
# note: Failed to solve saw hint and neetcode didnt understand so saw greg hogg and used his solution
#
# What went wrong in this first version:
# - Misindexed window: used `s2[r - l + 1]` as an INDEX (intended it as window length) → out-of-bounds risk.
# - Presence vs counts: checked membership (`x in s1`) instead of **frequency equality** → can’t detect permutations with duplicates.
# - Window control bug: resetting `l = r` whenever char “not in s1” nukes the window; this isn’t a fixed-size window of len(s1).
# - Nested while logic: `(r - l + 1) <= len(s1)` with inner `r += 1` can overrun and never properly slide by one.
# - No add/remove balance: never maintained character counts when moving `l` and `r`.
# - Performance: approaches O(n^2); no early guard for `len(s1) > len(s2)`.
#
# Key lesson:
# - Use a **fixed-size sliding window** of length `len(s1)` over `s2`, track **counts** (26-length arrays or dict),
#   and compare counts (or maintain a `matches` counter) as the window slides by **one** character each step.

        