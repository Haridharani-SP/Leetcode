class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #finding the peak element
        nums = [float("-inf"), *nums, float("-inf")]
        for i in range(1, len(nums)-1):
            if nums[i-1]<nums[i]>nums[i+1]:
                return i-1