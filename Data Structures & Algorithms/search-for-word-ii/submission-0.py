class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self,  words: List[str]):
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endWord = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.addWord(words)
        lengthofrow = len(board)
        lengthofcolumn = len(board[0])
        # I Had the idea to move +1 and -1 between Rows and Columns and solved until here I also had the idea to use index mapping to make sure the same node is not visited again like (0,0) or (0,1) or (1,0).
        res, visit = set(), set()
        def dfs(r: int, c: int, node: TrieNode, word: str) -> None:
            if (r < 0 or c < 0 or r >= lengthofrow or
                c >= lengthofcolumn or (r,c) in visit or
                board[r][c] not in node.children):

                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endWord:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(lengthofrow):
            for c in range(lengthofcolumn):
                dfs(r, c, self.root, "")
        return list(res)




        