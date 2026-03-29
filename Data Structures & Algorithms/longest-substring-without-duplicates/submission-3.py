class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l, r = 0, 0
        count = 0
        longest = 0
        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                count += 1
                longest = max(longest, count)
                r += 1
            else:
                hashset.remove(s[l])
                count -= 1
                l += 1
        return longest