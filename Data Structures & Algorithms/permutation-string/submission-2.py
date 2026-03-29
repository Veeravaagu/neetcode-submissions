class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hashmap = {}
        for char in s1:
            s1hashmap[char] = s1hashmap.get(char, 0) + 1
        s2hashmap = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] not in s1hashmap:
                l = r + 1
                s2hashmap.clear()
            else:
                s2hashmap[s2[r]] = s2hashmap.get(s2[r], 0) + 1
                if r - l + 1 > len(s1):
                    s2hashmap[s2[l]] -= 1
                    if s2hashmap[s2[l]] == 0:
                        del s2hashmap[s2[l]]
                    l += 1
                if s2hashmap == s1hashmap:
                    return True
        return False
                