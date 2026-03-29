class TimeMap:

    def __init__(self):
        self.obj = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.obj.setdefault(key, []).append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if self.obj.get(key):
            left = 0
            right = len(self.obj.get(key,[])) - 1
            while left <= right:
                mid = (left + right) // 2
                index = -1
                if self.obj[key][mid][0] > timestamp:
                    right = mid - 1
                elif self.obj[key][mid][0] <= timestamp:
                    left = mid + 1
                    index = mid
            if index == - 1:
                return ""
            else:
                return self.obj[key][mid][1]


        
