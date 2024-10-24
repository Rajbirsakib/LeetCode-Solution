class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            ans=0
            temp=x
            while temp!=0:
                a=temp%10
                ans=ans*10+a
                temp=temp//10
            return ans==x
        
        