class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
                left += 1
            else:
                right += 1