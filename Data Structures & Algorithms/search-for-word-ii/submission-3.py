class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, root, word):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in root.children or (r, c) in visit):
                return
            visit.add((r, c))
            root = root.children[board[r][c]]
            word += board[r][c]
            if root.isWord:
                res.add(word)

            dfs(r + 1, c, root, word)  
            dfs(r - 1, c, root, word) 
            dfs(r, c + 1, root, word) 
            dfs(r, c - 1, root, word)

            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)           

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, words):
        curr = self
        for c in words:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

            
        