class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        else:
            hashmap = { "]":"[", "}":"{", ")":"("}
            stack = []
            for ch in s:
                if ch in ["[", "{", "("]:
                    stack.append(ch)
                else:
                    peek = stack.pop()
                    if peek != hashmap[ch]:
                        return False
            return not stack

        