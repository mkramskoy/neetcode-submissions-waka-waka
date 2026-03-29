class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        # traversing rows
        for row in board:
            rowSet = set()
            for num in row:
                if num != '.' and num in rowSet:
                    isValid = False
                
                rowSet.add(num)

        # traversing columns
        for columnIndex in range(9):
            columnSet = set()
            for rowIndex in range(9):
                num = board[rowIndex][columnIndex]
                if num != '.' and num in columnSet:
                    isValid = False
                
                columnSet.add(num)

        # traversing 3x3s
        for squareRowIndex in range(3):
            for squareColumnIndex in range(3):
                squareSet = set()
                for i in range(3):
                    for j in range(3):
                        num = board[squareRowIndex*3+i][squareColumnIndex*3+j]
                        if num != '.':
                            if num in squareSet:
                                isValid = False
                            else:
                                squareSet.add(num)

        return isValid
                    
  
        
