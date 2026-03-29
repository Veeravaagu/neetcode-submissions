class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l, r = 0, 0
        longest = 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            while r - l + 1 - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
                
