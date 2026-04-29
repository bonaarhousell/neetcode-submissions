#breakdown:
#   input: string s and t
#   output: boolean
#   objective: can know if the string s is have words same as string t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}
        for word in s:
            if word in res:
                res[word] += 1
            else:
                res[word] = 1

        for x in t:
            if x in res:
                res[x] -= 1
            else:
                return False

        for x in res:
            if res[x] != 0:
                return False

        return True