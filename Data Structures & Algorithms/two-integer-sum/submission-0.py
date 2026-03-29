class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = target - nums[i]
            if j in nums:
                return [min(i,nums.index(j)), max(i,nums.index(j))]
        return [min(i,nums.index(j)), max(i,nums.index(j))]
        