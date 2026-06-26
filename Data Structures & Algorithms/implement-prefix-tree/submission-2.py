class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.endword = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            i = ord(w) - ord("a")
            if cur.children[i] == None:
                cur.children[i] = TreeNode()
            cur = cur.children[i]
        cur.endword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            i = ord(w) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.endword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            i = ord(p) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True
        