class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) == len(t):
            for i in s:
                if i in dict_s:
                    dict_s.update({i:dict_s[i]+1})
                else:
                    dict_s.update({i:1})
            for i in t:
                if i in dict_t:
                    dict_t.update({i:dict_t[i]+1})
                else:
                    dict_t.update({i:1})
            if dict_s == dict_t:
                return True
    
            return False
        return False
        