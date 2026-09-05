class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        newS = list(s)

        count = 0
        for x in t:
            if count == len(newS) - 1:
                return True
            if x == newS[count]:
                count+= 1

        return False
