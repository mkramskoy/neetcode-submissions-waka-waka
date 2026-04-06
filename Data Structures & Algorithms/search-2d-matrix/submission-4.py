class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            mid = l + int((r-l)/2)

            x, y = mid // n, mid % n

            if target == matrix[x][y]:
                return True
            if target < matrix[x][y]:
                r = mid - 1
            elif target > matrix[x][y]:
                l = mid + 1
        
        return False
        