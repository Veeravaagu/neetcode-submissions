class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # If array is already sorted (not rotated), do normal binary search.
        if nums[left] <= nums[right]:
            return self.binarysearch(nums, target, 0, len(nums) - 1)

        # Find pivot = index of smallest element.
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # Decide which sorted half to search.
        # Left half is [0 .. pivot-1], right half is [pivot .. n-1]
        if pivot > 0 and nums[0] <= target <= nums[pivot - 1]:
            return self.binarysearch(nums, target, 0, pivot - 1)
        else:
            return self.binarysearch(nums, target, pivot, len(nums) - 1)

    def binarysearch(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
# Solved 31 Minutes and took 6 Minutes to optimise see submitted solutions