class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        countS1 = [0] * 26
        countS2 = [0] * 26
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord("a")] += 1
            countS2[ord(s2[i]) - ord("a")] += 1
        if countS1 == countS2:
            return True
        
        for i in range(len(s1), len(s2)):
            countS2[ord(s2[i]) - ord("a")] += 1
            countS2[ord(s2[i - len(s1)]) - ord("a")] -= 1

            if countS1 == countS2:
                return True
        return False
        