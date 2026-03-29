class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                popped_index, popped_height = stack.pop()
                area = popped_height * (index - popped_index)
                maxArea = max(maxArea, area)
                start = popped_index
            stack.append([start, height])
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights) - i))
        return maxArea