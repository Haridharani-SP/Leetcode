class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()          # 1️⃣ sort to group duplicates
        res = []
        n = len(nums)

        def backtrack(start, path):
            res.append(path)

            for i in range(start, n):
                # 2️⃣ skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res
