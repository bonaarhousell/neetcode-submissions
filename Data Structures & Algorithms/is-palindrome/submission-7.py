class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for x in s:
            if x.isalnum():
                newstr += x.lower()
        print(newstr)

        l = 0
        r = len(newstr) - 1

        while l < r:
            if newstr[l] != newstr[r]:
                return False
            
            l += 1
            r -= 1
        return True