class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # got the logic but not the code for checking validity took 1:20 mins to do all this.
        m = len(s)
        n = len(t)
        need = {}
        window = {}
        missing = n
        best_len = float("inf")
        best_range = (0,0)
        if len(s) < len(t):
            return ""
        for i in range(n):
            need[t[i]] = need.get(t[i], 0) + 1
        l = 0
        r = 0
        for r in range(m):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if window[c] <= need.get(c, 0):
                missing -= 1
            while missing == 0:
                if (r - l + 1) < best_len:
                    best_len = (r - l + 1)
                    best_range = (l, r)
                d = s[l]
                if window[d] <= need.get(d, 0):
                    missing += 1
                window[d] -= 1
                l += 1
            r += 1
        return "" if best_len == float("inf") else s[best_range[0]:best_range[1] + 1]

             



        