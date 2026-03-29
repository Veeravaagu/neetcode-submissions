class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op ={}
        arr = []
        array = []
        word_count = 1
        for word in strs:
            letter_count = 1
            output = {}
            for letter in word:
                if letter in output:
                    letter_count+=1
                    output.update({letter:letter_count})
                else:
                    output[letter] = letter_count
            if output not in arr:
                arr.append(output)
                array.append([word])
            else:
                k = arr.index(output)  
                array[k].append(word)
        return array
        
        