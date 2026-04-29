class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        k = 0
        r1 = len(word1) - 1
        r2 = len(word2) - 1
        mword = []
        while i <= r1 or i <= r2:
            if i > r1:
                mword.append(word2[i])
            elif k > r2:
                mword.append(word1[k])
            else:
                mword.append(word1[i])
                mword.append(word2[k])

            i += 1
            k += 1
        res = "".join(mword)
        return res