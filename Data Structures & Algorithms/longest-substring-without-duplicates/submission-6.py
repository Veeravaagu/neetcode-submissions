class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        hashset = set()
        for r in range(len(s)):
            if s[r] not in hashset:
                hashset.add(s[r])
                longest = max(longest, r - l + 1)
            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
                hashset.add(s[r])
        return longest        