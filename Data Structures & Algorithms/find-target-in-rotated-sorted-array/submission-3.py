class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
        else:
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            pivot = left
            if target <= nums[pivot -1] and target >= nums[0]:
                left = 0
                right = pivot - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] > target:
                        right = mid - 1
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        return mid
            else:
                left = pivot
                right = len(nums) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] > target:
                        right = mid - 1
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        return mid
        return -1


        