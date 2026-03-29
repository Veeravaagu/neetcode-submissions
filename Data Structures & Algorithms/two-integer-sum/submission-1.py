class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = target - nums[i]
            nums.remove(nums[i])
            if j in nums:
                return [min(i,nums.index(j)+1), max(i,nums.index(j)+1)]
        return [min(i,nums.index(j)+1), max(i,nums.index(j)+1)]
        