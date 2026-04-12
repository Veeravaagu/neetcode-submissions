class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combSet = []
        def dfs(i, combSum):
            if combSum == target:
                res.append(combSet.copy())
                return 
            if i == len(nums) or combSum > target:
                return
            combSum += nums[i]
            combSet.append(nums[i])
            dfs(i, combSum)

            combSum -= combSet.pop()
            dfs(i + 1, combSum)
        dfs(0, 0)
        return res
        