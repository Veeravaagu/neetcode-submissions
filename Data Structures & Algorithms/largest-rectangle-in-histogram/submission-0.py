class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
                #Couldn't find a solution in 20 Mins saw NeetCode and wrote code had errors so used GPT and Neetcode Solution
        stack = []
        maxArea = 0
        for i,h in enumerate (heights):
            start = i
            while stack and h < stack[-1][1]:
                last_index, last_height = stack.pop()
                maxArea = max(maxArea,last_height*(i-last_index))
                start = last_index
            stack.append([start,h])
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights) - i))
        return maxArea
        