class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums1=set(nums)
        nums1=list(nums1)
        nums1=sorted(nums1)
        if len(nums1)<=2:
            return nums1[-1]
        if len(nums1)>=5:
           return nums1[-3]
        if len(nums1)==4:
            return nums1[1]
        if len(nums1)==3:
            return nums1[0]