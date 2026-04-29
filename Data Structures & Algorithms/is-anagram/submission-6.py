#breakdown:
#   input: string s and t
#   output: boolean
#   objective: can know if the string s is have words same as string t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for x in s:
            if x in map:
                map[x] += 1
            else:
                map[x] = 1
        
        for i in t:
            if i in map:
                map[i] -= 1
        print(map)
        for key in map:
            if map[key] != 0:
                return False
        return True
        

                