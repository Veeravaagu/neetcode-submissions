class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = {}
        columnHash = {}
        boxHash ={}
        for i in range (9):
            rowHash.clear()
            columnHash.clear()
            boxHash.clear()
            for j in range(9):
                x=board[i][j]
                y = board[j][i]
                rowHash[x] = rowHash.get(x,0)+1
                columnHash[y] = columnHash.get(y,0)+1
    #CHATGPT
            br = (i // 3) * 3   
            bc = (i % 3) * 3
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    z = board[r][c]
                    if z != '.':
                        boxHash[z] = boxHash.get(z, 0) + 1
            rowHash.pop('.')
            columnHash.pop('.')
            if 2 in rowHash.values():
                return False
            if 2 in columnHash.values():
                return False
            if 2 in boxHash.values():
                return False
        return True
        