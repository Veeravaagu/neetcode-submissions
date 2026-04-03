class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        hashmapT = {}
        hashmapS = {}
        for i in range(len(t)):
            hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1
        seen = len(hashmapT)
        res = [-1, -1]
        resLen = float("inf")
        visit = 0
        l = 0
        for r in range(len(s)):
            hashmapS[s[r]] = hashmapS.get(s[r], 0) + 1
            if s[r] in hashmapT:
                if hashmapT[s[r]] == hashmapS[s[r]]:
                    visit += 1
                    while seen == visit:
                        if r - l + 1 < resLen:
                            res = [l, r]
                            resLen = r - l + 1
                        hashmapS[s[l]] -= 1
                        if s[l] in hashmapT and hashmapS[s[l]] < hashmapT[s[l]]:
                            visit -= 1
                        l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""