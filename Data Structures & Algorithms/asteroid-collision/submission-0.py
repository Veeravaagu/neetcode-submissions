class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            while stack and stack[-1] > 0 and n < 0:
                if stack[-1] < -n:
                    stack.pop()
                    continue
                elif stack[-1] == -n:
                    stack.pop()
                break
            else:
                stack.append(n)
        return stack
        