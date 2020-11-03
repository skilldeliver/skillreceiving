# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

class Solution(object):
    @staticmethod
    def isValidRow(row):
        digits = [d for d in row if d.isdigit()]

        if len(digits) != len(set(digits)):
            return False
        return True

    @staticmethod
    def isValidColumn(col, board):
#        digits = [r[col] for r in board if r[col].isdigit()]
        digits = list()

        for row in board:
            if row[col].isdigit():
                digits.append(row[col])

        if len(digits) != len(set(digits)):
            return False
        return True

    @staticmethod
    def isValidNineBox(row):
        for j in range(3, 10, 3):
            box = list()

            for k in range(3):
                for item in row[k][j-3:j]:
                    if item.isdigit():
                        box.append(item)

            #box = [item for k in range(3) for item in row[k][j-3:j] if item.isdigit()]
            if len(box) != len(set(box)):
                return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for row in board:
            if not Solution.isValidRow(row):
                return False

        for col in range(9):
            if not Solution.isValidColumn(col, board):
                return False

        for i in range(3, 10, 3):
            row = board[i-3:i]
            if not Solution.isValidNineBox(row):
                return False

        return True
