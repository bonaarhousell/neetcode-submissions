class TrieRoot:
    def __init__(self):
        self.trie = {}
        self.endpath = False

class Solution:
    def __init__(self):
        self.root = TrieRoot()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        for fold in folder:
            cur = self.root
            f = fold.split("/")[1:]
            for i in range(len(f)):
                if f[i] not in cur.trie and not cur.endpath:
                    cur.trie[f[i]] = TrieRoot()
                if cur.trie:
                    cur = cur.trie[f[i]]
                if i + 1 == len(f):
                    cur.endpath = True

        res = []
        for fold in folder:
            dum = self.root
            f = fold.split("/")[1:]
            for i in range(len(f)):
                if f[i] not in dum.trie:
                    dum.trie[f[i]] = TrieRoot()
                dum = dum.trie[f[i]]
            if dum.endpath:
                res.append(fold)

        return res
