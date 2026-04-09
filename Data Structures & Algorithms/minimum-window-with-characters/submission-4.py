class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countS, countT = {}, {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        need = len(countT)
        have = 0
        res = [-1, -1]
        resLen = float("inf")
        l = 0
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0) + 1
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1
                while have == need:
                    if resLen > r - l + 1:
                        res = [l, r]
                        resLen = r - l + 1
                    countS[s[l]] -= 1
                    if s[l] in countT and countT[s[l]] > countS[s[l]]:
                        have -= 1
                    l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
                
        
        
        