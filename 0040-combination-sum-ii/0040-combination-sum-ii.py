class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(start, path, total):
            if total == target:
                res.append(path.copy())
            if total > target:
                return
            for i in range(start,n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                x = candidates[i]
                dfs(i+1, path + [x], total + x)
        dfs(0,[],0)
        return res