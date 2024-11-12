class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_p=prices[0]
        ans=0
        for i in prices[1:]:
            if b_p > i:
                b_p=i
            ans=max(ans, i-b_p)
        return ans