class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp =  n
        revese = 0
        while temp > 0:
            digit = temp % 10
            revese = revese *10 + digit
            temp = temp // 10

        return abs(n - revese)