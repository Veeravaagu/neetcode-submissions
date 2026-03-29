class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*(len(nums)+1)
        postfix = [1]*(len(nums)+1)
        for i in range (0,len(nums)):
            output[i] = nums[i]*output[i-1]
        for i in range (len(nums)-1,-1,-1):
            postfix[i] = nums[i]*postfix[i+1]
        res = [0]*len(nums)
        for i in range (len(nums)):
            res[i] = output[i-1]*postfix[i+1]
        return res