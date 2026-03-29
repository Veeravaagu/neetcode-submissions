class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        column = len(matrix[0])

        n = rows * column
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // column][mid % column] > target:
                right = mid - 1
            elif matrix[mid // column][mid % column] < target:
                left = mid + 1
            else:
                return True
        return False
        