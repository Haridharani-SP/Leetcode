class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l1=list(permutations(nums))
        return list(set(l1))