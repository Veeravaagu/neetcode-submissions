class Solution:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, words: List[str]):
        for char in words:
            curr = self.root
            for c in char:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.addWord(words)
        ROWS = len(board)
        COLS = len(board[0])
        res, visited = set(), set()
        def dfs(r, c, curr, char):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or (r, c) in visited or board[r][c] not in curr.children):


                return
            visited.add((r, c))
            curr = curr.children[board[r][c]]
            char += board[r][c]
            if curr.word:
                res.add(char)
            dfs(r + 1, c, curr, char)
            dfs(r - 1, c, curr, char)
            dfs(r, c + 1, curr, char)
            dfs(r, c - 1, curr, char)
            visited.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, self.root, "")
        return list(res)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
