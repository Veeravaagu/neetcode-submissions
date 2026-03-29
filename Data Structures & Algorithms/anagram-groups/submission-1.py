class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op ={}
        arr = []
        array = []
        for word in strs:
            output = {}
            for letter in word:
                if letter in output:
                    output[letter] = output.get(letter, 0) + 1
                else:
                    output[letter] = output.get(letter, 1)
            if output not in arr:
                arr.append(output)
                array.append([word])
            else:
                k = arr.index(output)  
                array[k].append(word)
        return array
        
        