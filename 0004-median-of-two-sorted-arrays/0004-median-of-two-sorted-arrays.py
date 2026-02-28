class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #using sort function
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:
            a=nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1]
            return a/2
        else:
            return nums1[len(nums1)//2]
        