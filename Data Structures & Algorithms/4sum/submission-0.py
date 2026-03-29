class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if left == i or left == j:
                        left += 1
                    elif right == i or right == j:
                        right -= 1
                    else:
                        if nums[left] + nums[right] > target - nums[i] - nums[j]:
                            right -= 1
                        elif nums[left] + nums[right] < target - nums[i] -nums[j]:
                            left += 1
                        else:
                            res.append([nums[left], nums[right], nums[i], nums[j]])
                            while left < right and nums[left] == nums[left + 1]:
                                left += 1
                            while left < right and nums[right] == nums[right - 1]:
                                right -= 1
                            left += 1
                            right -=1
        return res
# NOTES FOR FUTURE ME (Four Sum attempt):

# 1. I initialized left = 0 and right = len(nums) - 1 for every (i, j).
#    This forced me to manually skip indices i and j using conditions.
#    The correct approach is: left = j + 1 and right = n - 1.
#    That automatically avoids reusing i and j.

# 2. Because of the wrong left/right initialization, I added checks like:
#       if left == i or left == j
#       if right == i or right == j
#    These are unnecessary if left starts at j + 1.

# 3. My outer loops ran too far:
#       for i in range(len(nums))
#       for j in range(i + 1, len(nums))
#    But Four Sum needs space for two more numbers.
#    Correct limits:
#       i in range(n - 3)
#       j in range(i + 1, n - 2)

# 4. After finding a valid quadruplet I appended it but did not move the pointers.
#    This can cause infinite loops or repeated results.
#    After a match I must move both pointers.

# 5. I did not handle duplicates for i, j, left, and right.
#    Without skipping duplicates the result list will contain repeated quadruplets.

# 6. The quadruplet order I appended was inconsistent:
#       [nums[left], nums[right], nums[i], nums[j]]
#    It is cleaner and easier for duplicate handling to append in sorted order:
#       [nums[i], nums[j], nums[left], nums[right]]

# 7. The array must be sorted before using the two-pointer technique.
#    I correctly added nums.sort(), which is required for the pointer logic to work.

# Summary of improvement goal:
# Fix two numbers (i, j), then run a standard two-pointer search
# on the remaining sorted portion of the array: [j+1 ... n-1].



                    
        