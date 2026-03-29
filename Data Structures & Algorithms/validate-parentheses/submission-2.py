class Solution:
    def isValid(self, s: str) -> bool:
        #Used GPT and solved
        if len(s)%2 != 0:
            return False
        else:
            hashmap = { "]":"[", "}":"{", ")":"("}
            stack = []
            for ch in s:
                if ch in hashmap.values():
                    stack.append(ch)
                else:
                    if not stack or stack.pop() != hashmap[ch]:
                        return False
            return not stack

        