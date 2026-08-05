class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split()
        string = string[::-1]
        mstr = ''
        for st in string:
            mstr += st
            mstr += ' '
        
        return mstr.strip(" ")
        