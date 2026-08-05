import math as m
class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn = n
        if nn<0:
            nn *= -1
        ans = 1.0
        while nn>0:
            if nn % 2 == 0:
                x *= x
                nn /=2
            else:
                ans *= x
                nn -=1
        if n<0:
            return 1/ans
        else:
            return ans
        
