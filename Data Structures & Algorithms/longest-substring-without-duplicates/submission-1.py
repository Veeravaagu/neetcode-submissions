class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        k = 0
        substr = []
        while r < len(s):
            if s[r] not in substr:
                substr.append(s[r])
                r += 1
                k = max(k, len(substr))
            else:
                substr.remove(s[l])
                l += 1
        return k
# doc: sliding-window (list-based) submission — 2025-09-29
#
# Problem: Longest Substring Without Repeating Characters.
# Approach here:
# - Maintain a window [l, r) and a LIST `substr` holding the current window’s chars.
# - Expand r while s[r] not in `substr`; append it, update best length `k`.
# - On duplicate, shrink from the left: remove the LEFTMOST char (`s[l]`) from `substr`, then l += 1.
#
# What I fixed vs earlier attempts:
# - Check membership on the CHARACTER (s[r]), not the index r.
# - Drive the loop with `while r < len(s)` (not `l < r`).
# - When shrinking, remove by VALUE (`substr.remove(s[l])`) instead of indexing with l (which caused IndexError).
# - Keep shrinking until the duplicate is gone (via the loop structure).
#
# Complexity note:
# - `s[r] in substr` and `substr.remove(...)` are O(n) with a LIST ⇒ overall worst-case O(n^2).
# - OK for n ≤ 1e3, but not optimal.
#
# Next iteration (performance):
# - Use a SET for membership (O(1)) and move l/r pointers → overall O(n).
#   Or use a dict {char: last_index} and jump l = max(l, last_index+1).
#
# Quick test set:
# - "", "a", "aaaa"→1, "abba"→2, "abcabcbb"→3, "pwwkew"→3, "zxyzxyz"→3
#
# Takeaway:
# - This version is correct and readable; future improvement is to swap LIST membership for SET/dict to hit O(n).



            
        