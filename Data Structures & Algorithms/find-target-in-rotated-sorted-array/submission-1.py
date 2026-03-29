class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Took 45 mins to think because leetcode question explanation confused me and almost found the solution but made small mistakes check neetcode submission for mistakes and changes made.
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


