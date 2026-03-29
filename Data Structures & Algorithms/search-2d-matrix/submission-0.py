class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Did Brute Force but recognised the pattern that we should somehow append the row and column to get one big sorted array but didn't know how, used GPT to find it.
        m, n = len(matrix),len(matrix[0])
        left, right = 0, m*n - 1
        while left <= right:
            mid = (left + right)//2
            r, c = divmod(mid, n)
            if matrix[r][c] < target:
                left = mid + 1 
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #leftPtrRow = 0
        #rightPtrRow = len(matrix) - 1
        #while leftPtrRow <= rightPtrRow:
            #midOfRow = (leftPtrRow + rightPtrRow)//2
            #if matrix[midOfRow][0] < target and matrix[midOfRow][-1] < target:
                #leftPtrRow = midOfRow + 1
            #elif matrix[midOfRow][0] > target and matrix[midOfRow][-1] > target:
                #rightPtrRow = midOfRow - 1
            #else:
                #leftPtrCol, rightPtrCol = 0, len(matrix[midOfRow])-1
                #while leftPtrCol <= rightPtrCol:
                    #midOfCol = (leftPtrCol + rightPtrCol)//2
                    #if matrix[midOfRow][midOfCol] < target:
                        #leftPtrCol = midOfCol + 1
                    #elif matrix[midOfRow][midOfCol] > target:
                        #rightPtrCol = midOfCol - 1
                    #else:
                        #return True
        #return False

        