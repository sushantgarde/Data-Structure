class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if len(s) == 0:
        #     return True
        # s = s.lower()
        # s = "".join(s.split())

        # import re
        # s = re.sub(r'[^a-zA-Z0-9]', '', s)

        # # print(s)
        # # print("Reversed", s[::-1])
        # if s == s[::-1]:
        #     return True
        # else:
        #     return False
        res="".join([char for char in s if char.isalnum()])
        res=res.lower()
        return res==res[::-1]