class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp= sorted(nums)
        dic={}

        for i in range(len(temp)):
            if temp[i] not in dic:
                dic[temp[i]]=i
        
        ret=[]
        for i in range (len(nums)):
            ret.append(dic[nums[i]])
        return ret