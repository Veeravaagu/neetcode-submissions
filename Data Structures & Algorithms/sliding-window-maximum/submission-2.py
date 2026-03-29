class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #some syntax and logic errors but minimal errors | O(n.k)
        res = []
        window = deque()
        l = 0
        r = 0
        for r in range(len(nums)):
            while window and nums[window[-1]] <= nums[r]:
                window.pop()
            window.append(r)
            if window and window[0] < r - k + 1:
                window.popleft()
            if r >= k - 1:
                res.append(nums[window[0]])
        return res


