class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(i, combSum):
            if combSum == target:
                res.append(comb.copy())
                return
            if combSum > target:
                return
            if i == len(nums):
                return
            comb.append(nums[i])
            combSum += nums[i]
            dfs(i, combSum)

            combSum -= comb.pop()
            dfs(i + 1, combSum)
        dfs(0, 0)
        return res
