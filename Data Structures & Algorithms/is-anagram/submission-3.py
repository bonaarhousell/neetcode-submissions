class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        words = {}
        for i in range(len(s)):
            words[s[i]] = words.get(s[i], 0) + 1
            words[s[i]] = words.get(s[i], 0) - 1
            for word in s:
                words[word] = 1

        for w in t:
            if w not in words:
                return False
        return True
                