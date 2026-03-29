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


            
        