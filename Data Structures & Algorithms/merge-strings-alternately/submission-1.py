class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r1 = len(word1) - 1
        r2 = len(word2) - 1

        l = 0
        j = 0
        word = ""

        while l <= r1 or j <= r2:
            if l > r1:
                word += word2[j]
                j += 1
            elif j > r2:
                word += word1[l]
                l += 1
            else:
                word += word1[l] + word2[j]
                l += 1
                j += 1
        return word