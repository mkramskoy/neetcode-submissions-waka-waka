class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        # traversing rows
        for row in board:
            rowDict = {}
            for num in row:
                if num != '.' and num in rowDict:
                    isValid = False
                
                rowDict[num] = 1

        # traversing columns
        for columnIndex in range(9):
            columnDict = {}
            for rowIndex in range(9):
                num = board[rowIndex][columnIndex]
                if num != '.' and num in columnDict:
                    isValid = False
                
                columnDict[num] = 1

        # traversing 3x3s
        for squareRowIndex in range(3):
            for squareColumnIndex in range(3):
                squareDict = {}
                for i in range(3):
                    for j in range(3):
                        num = board[squareRowIndex*3+i][squareColumnIndex*3+j]
                        if num != '.':
                            if num in squareDict:
                                isValid = False
                            else:
                                squareDict[num] = 1
                        
                

        return isValid
                    
  
        
