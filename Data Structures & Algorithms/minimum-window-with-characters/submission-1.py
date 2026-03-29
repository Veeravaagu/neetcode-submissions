class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

        
#1. Create a hashmap of counts for t
#2. Iterate using a for loop through s
#3. Add counts of the alphabets that are in t if we find a duplicate alphabet update the existing location of that to the newest position found.
#4. Continue until all the alphabets of t is seen from s. If even a single alphabet is missing return "" else return the string starting from and ending from.
#5. Hashmap -> we need two one to store string t and another hashmap where we only add the elements if they are present in hashmap for t and if the counts match.
#6. for example let us say they are x: 3 in hashmap t and x: 3 we add another x but remove the first x we saw, for this maintain an array of values of the position and append to it as you see the elements
