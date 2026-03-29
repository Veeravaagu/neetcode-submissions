class Solution:
    def findMin(self, nums: List[int]) -> int:
        #left, right = 0, len(nums) - 1
        # I want to check if it is rotated n-times
        #if nums[left] < nums[right]:
            #return nums[left]
        # for other cases I can skip the else just write while
        # I want to move left and right based on mid if it is increasing i move right to mid if left to mid.
        #while left <= right:
            #mid = (left + right) // 2
            #if nums[left] > nums[right] and nums[left] > nums[mid] or nums[right] < nums[mid]:
                #right = mid
            #elif nums[right] > nums[left] and nums[right] > nums[mid] or nums[left] < nums[mid]:
                #left = mid
            #else:
                #return min(nums[left], nums[right], nums[mid])
        left, right = 0, len(nums) - 1

        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]    

# See commented code took 45 mins and so saw the solution using GPT
    