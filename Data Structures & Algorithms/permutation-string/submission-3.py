class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = {}
        for i in range(len(s1)):
            hashmap_s1[s1[i]] = hashmap_s1.get(s1[i], 0) + 1
        hashmap_s2 = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] not in hashmap_s1:
                l = r + 1
                hashmap_s2.clear()
            else:
                hashmap_s2[s2[r]] = hashmap_s2.get(s2[r], 0) + 1
                if r - l + 1 > len(s1):
                    hashmap_s2[s2[l]] -= 1
                    if hashmap_s2[s2[l]] == 0:
                        del hashmap_s2 [s2[l]]
                    l += 1 
                if hashmap_s2 == hashmap_s1:
                    return True
        return False
                