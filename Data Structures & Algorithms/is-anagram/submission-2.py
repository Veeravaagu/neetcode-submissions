class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        for i in range (len(s)):
            hashmap_s[s[i]] = hashmap_s.get(s[i], 0) + 1
        for j in range (len(t)):
            hashmap_t[t[j]] = hashmap_t.get(t[j], 0) + 1
        if hashmap_s == hashmap_t:
            return True
        else:
            return False

        