class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Found The Logic but didn't know how to connect position with speed and time so used GPT.
        cars = sorted(zip(position, speed), key=lambda ps: ps[0], reverse=True)
        last_time = 0
        fleets = 0
        for p,s in cars:
            t = (target - p) / s
            if t > last_time:
                fleets += 1
                last_time = t
        return fleets
        