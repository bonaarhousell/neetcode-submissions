class Trie:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.endword = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for w in range(j, len(word)):
                i = word[w]
                if i == ".":
                    for child in node.children.values():
                        if dfs(w + 1, child):
                            return True
                    return False
                else:
                    if i not in node.children:
                        return False
                    node = node.children[i]
            return node.endword


        return dfs(0, self.root)



