# Was able to solve addWord but not search didn't have any idea to use recursion
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endWord = True
        return
    def search(self, word: str) -> bool:
        def dfs(index, child):
            curr = child
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                        return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endWord
        return dfs(0, self.root)
        
