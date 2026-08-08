class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        
        # Iterate through each character position in the first string
        for col in range(len(strs[0])):
            char = strs[0][col]
            
            # Check this character against all other strings
            for row in range(1, len(strs)):
                # If this string is shorter or character doesn't match, stop
                if col >= len(strs[row]) or strs[row][col] != char:
                    return strs[0][:col]
        
        # If we exit without mismatch, the entire first string is the prefix
        return strs[0]        