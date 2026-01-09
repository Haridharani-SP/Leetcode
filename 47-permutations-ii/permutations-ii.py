class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res =[]
        n=len(nums)
        used=[False]*n
        def dfs(path):
            if len(path)==n:
                res.append(path.copy())
                return
            for i in range(n):
                x=nums[i]
                if used[i]==True:
                    continue
                used[i]=True
                dfs(path+[x] )
                used[i]=False
        dfs([])
        res1=[]
        for i in res:
            res1.append(tuple(i))
        return list(set(res1))

        