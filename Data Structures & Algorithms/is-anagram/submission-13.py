#breakdown:
#   input: string s and t
#   output: boolean
#   objective: can know if the string s is have words same as string t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for x in s:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        for x in t:
            if x in freq:
                freq[x] -= 1
            else:
                return False
            if freq[x] < 0:
                return False
        return True
