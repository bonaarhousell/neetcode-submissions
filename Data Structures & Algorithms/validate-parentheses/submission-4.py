class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        op = []

        for brac in s:
            if brac in mp:
                if op and op[-1] == mp[brac]:
                    op.pop()
                else:
                    return False
            else:
                op.append(brac)

        if not op:
            return True
        else:
            return False