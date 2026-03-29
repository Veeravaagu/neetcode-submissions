class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = target - nums[i]
            num = nums.copy()
            num.remove(num[i])
            if j in num:
                return [min(i,num.index(j)+1), max(i,num.index(j)+1)]
        return [min(i,num.index(j)+1), max(i,num.index(j)+1)]
        