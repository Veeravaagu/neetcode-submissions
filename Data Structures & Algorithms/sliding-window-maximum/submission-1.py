class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()
        l = 0
        r = 0
        for r in range (k):
            window.append(nums[r])
        res.append(max(window))
        for r in range(k, len(nums)):
            window.popleft()
            l += 1
            window.append(nums[r])
            res.append(max(window))
        return res


