class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n= len(nums2)
        l=[]
        for i in range(len(nums1)):
            max_val=-1
            b=0
            for j in range(n):
                if nums1[i]==nums2[j]:
                    b=1
                if b==1 and nums2[j]>nums1[i]:
                    max_val=nums2[j]
                    break
            l.append(max_val)
        return l

        