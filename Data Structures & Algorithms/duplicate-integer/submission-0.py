class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        sett = set()
        for i in range (n):
            sett.add(nums[i])
            print (sett)
        if len(sett) == n:
            value = False
        else:
            value = True
        return value