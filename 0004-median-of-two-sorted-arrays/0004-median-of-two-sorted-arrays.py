class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+nums2
        total=len(arr)
        arr.sort()
        if total%2==0:
            m1= float(arr[total//2-1])
            m2= float(arr[total//2])
            return (float(m1+m2))/2
        else:
            return float(arr[total//2])
        
        