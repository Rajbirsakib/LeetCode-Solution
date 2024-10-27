class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list=[]
        n=len(nums)
        list1=set(nums)
        for i in range(1,n+1):
            if i not in list1:
                list.append(i)
        
        return list
        