class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                if s[l] == s[r - 1]:
                    return True
                elif s[l + 1] != s[r]:
                    return False
                elif s[l + 1] != s[r - 1]:
                    return False
                else:
                    return True
            l += 1
            r -= 1
        return True