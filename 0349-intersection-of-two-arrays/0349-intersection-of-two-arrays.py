class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=set(nums1)
        y=set(nums2)
        nums=[]
        for num in y:
            if num in x:
                nums.append(num)

        return nums