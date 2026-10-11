class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currentRow = 0
        goingDown = False

        for c in s:
            rows[currentRow] += c

            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown

            if goingDown:
                currentRow += 1
            else:
                currentRow -= 1

        return "".join(rows)