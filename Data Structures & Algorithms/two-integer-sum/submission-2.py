class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = target - nums[i]
            num = nums.copy()
            num.remove(num[i])
            if j in num:
                return [min(i,nums.index(j)), max(i,nums.index(j))]
        return [min(i,nums.index(j)), max(i,nums.index(j))]
        