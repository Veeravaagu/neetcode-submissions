class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combSet = []

        def dfs(start, combSum):
            if combSum == target:
                res.append(combSet.copy())
                return
            if combSum > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue

                combSet.append(candidates[i])
                dfs(i + 1, combSum + candidates[i])
                combSet.pop()

                prev = candidates[i]

        dfs(0, 0)
        return res