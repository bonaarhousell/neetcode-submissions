class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        s = "".join(char for char in s if char.isalnum())

        for i in range(len(s)):
            j = len(s) -1 - i
            if s[i] != s[j]:
                return False

        return True
