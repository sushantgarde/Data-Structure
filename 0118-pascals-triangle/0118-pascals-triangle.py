class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = [1]
            res = 1

            for j in range(1, i+1):
                res = res * (i - j + 1) // j
                row.append(res)

            result.append(row)
        return result