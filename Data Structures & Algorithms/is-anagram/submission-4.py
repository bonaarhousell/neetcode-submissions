#breakdown:
#   input: string s and t
#   output: boolean
#   objective: can know if the string s is have words same as string t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for x in s:
            if x in map:
                map[x] += 1
            else:
                map[x] = 1
        
        for i in map:
            if i in t:
                map[i] += 1
            else:
                return False
        return True

                