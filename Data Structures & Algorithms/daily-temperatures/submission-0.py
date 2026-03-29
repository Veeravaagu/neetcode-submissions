class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Couldn't solve in 30 mins saw all hints
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):  
            while stack and temperatures[i] > temperatures[stack[-1]]:
                peek = stack.pop()
                result[peek] = (i - peek)
            stack.append(i)
        return result





        