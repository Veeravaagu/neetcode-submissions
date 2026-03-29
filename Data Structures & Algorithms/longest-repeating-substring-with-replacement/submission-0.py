class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        hashmap = {}
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
# fix: 424 — Character Replacement sliding window; stop tracking “replaced” positions
#
# Context (2025-09-29):
# - Problem: Longest Repeating Character Replacement.
# - Goal: longest window that can be made all one letter with ≤ k changes.
#
# What went wrong earlier:
# 1) Tried to track WHICH letters used up k — unnecessary and hard to maintain.
# 2) Used dict.get(...) + 1 without assignment → counts never changed.
# 3) Bad init once: `l, r = 0, l`; also referenced `k` before defining in a draft.
# 4) Logic attempted pops/deletes keyed by string indices instead of window counts.
# 5) Considered “releasing k” manually; the math already handles it.
#
# Correct invariant:
# - Let window_len = r - l + 1
# - Let max_freq = max count of any single char in the current window
# - Replacements needed = window_len - max_freq  (must be ≤ k)
# - If it exceeds k, move l right (decrement count of s[l]) until valid again.
#
# Implementation notes (no code here):
# - Maintain counts: dict[char] -> freq in window.
# - Update `max_freq` as we expand (can be slightly stale; still OK for correctness).
# - On each step: expand r, update counts/max_freq, shrink while invalid, update best length.
#
# Complexity:
# - Time: O(n) over the string (alphabet is fixed size, 26).
# - Space: O(1) w.r.t. alphabet (O(26)) or O(min(n, 26)).
#
# Edge cases / tests:
# - "ABAB", k=2 → 4
# - "AABABBA", k=1 → 4
# - All same chars (e.g., "AAAA", any k) → len(s)
# - k=0 behaves like longest run of identical chars
# - Long stretches where the majority letter changes mid-window
#
# Takeaway:
# - Don’t tag specific replaced positions. Count chars, track max_freq, and use
#   (window_len - max_freq ≤ k) to expand/shrink the window.






        