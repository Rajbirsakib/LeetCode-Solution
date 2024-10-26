class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        for i,n in enumerate(nums,0):
            if i!=n:
                return n-1
                
            if n==len(nums)-1:
                return n+1
        