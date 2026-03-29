class TimeMap:
    # Solved in 1:30
# Thought of using arrays first but decided to use hashmaps then reverted, Also the question was confusing so saw the discussions tab in leetcode and got a hint to map keys to timestamp and values. Used GPT a lot for syntax.
    def __init__(self):
        self.obj = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.obj.setdefault(key, []).append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if self.obj.get(key):
            left = 0
            right = len(self.obj.get(key, [])) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if self.obj[key][mid][0] > timestamp:
                    right = mid - 1
                elif self.obj[key][mid][0] <= timestamp:
                    left = mid + 1
                    index = mid
            if index == -1:
                return ""
            else:
                return self.obj[key][index][1]
        return ""


        
