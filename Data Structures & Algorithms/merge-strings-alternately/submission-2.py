class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r1, r2 = len(word1) - 1, len(word2) - 1

        l, r = 0, 0
        word = ""
        while l <= r1 or r <= r2:
            if l > r1:
                word += word2[r]
                r += 1
            elif r > r2:
                word += word1[l]
                l += 1
            else:
                word += word1[l] + word2[r]
                l += 1
                r += 1

        return word