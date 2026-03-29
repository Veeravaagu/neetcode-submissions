class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        res = [0] * len(temperatures)
        for index, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                res[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            stack.append([num, index])
        return res


        