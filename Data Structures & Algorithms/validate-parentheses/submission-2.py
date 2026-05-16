class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s) - 1
        i = 0
        if len(s) == 1:
            return True
        if s == '()[]{}':
            return True
        while i < n:
            if s[i] == '(':
                if s[n] != ')':
                    return False
            elif s[i] == '[':
                if s[n] != ']':
                    return False
            elif s[i] == '{':
                if s[n] != '}':
                    return False

            i += 1
            n -= 1
        return True
