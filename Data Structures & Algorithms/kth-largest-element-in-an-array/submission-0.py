class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        heapq.heapify((nums))
        ans = heapq.heappop(nums)
        while True:
            k -= 1
            if k == 0:
                return -ans
                break
            ans = heapq.heappop(nums)