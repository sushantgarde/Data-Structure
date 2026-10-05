class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if str(x) == str(x)[::-1]:
        #     return True
        # else:
        #     return False
        firstnum=str(x)
        newnum=firstnum[::-1]

        if newnum==firstnum:
            return True
        else:
            return False
        