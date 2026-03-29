class Solution:
    def isPalindrome(self, s: str) -> bool:
        #CHATGPT
        strs= ''.join(char for char in s if char.isalnum()).lower()
        #CHATGPT
        left = 0
        right = len(strs) - 1
        while left < right:
            if strs[left] == strs[right]:
                left += 1
                right += -1
            else:
                return False
        return True
        