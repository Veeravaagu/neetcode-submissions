class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        min_time = float('-inf')
        fleet_size = 0
        for car in range(len(position)):
            time = (target - position[car]) / speed[car] 
            stack.append([position[car], time])
        stack.sort()
        while stack:
            if stack[-1][1] > min_time:
                fleet_size += 1
                min_time = max(min_time, stack[-1][1])
                stack.pop()
            else:
                stack.pop()
        return fleet_size
        