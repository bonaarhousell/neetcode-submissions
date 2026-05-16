class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words = {}
        for word in s:
            words[word] = 1

        for w in t:
            if w not in words:
                return False
        return True
                