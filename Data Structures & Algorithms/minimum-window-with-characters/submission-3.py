class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        countS = {}
        res, resLen = [-1, -1], float("inf")
        l = 0
        have, need = 0, len(countT)
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0) + 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
                while have == need:
                    if r - l + 1 < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                    countS[s[l]] -= 1
                    if s[l] in countT and countS[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""


        