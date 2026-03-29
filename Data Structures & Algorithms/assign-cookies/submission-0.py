class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        childptr, cookieptr = 0, 0
        res = 0
        while childptr < len(g) and cookieptr < len(s):
            if s[cookieptr] >= g[childptr]:
                childptr += 1
                cookieptr += 1
                res += 1
            else:
                cookieptr += 1
        return res
        