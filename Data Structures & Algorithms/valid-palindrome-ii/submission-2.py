class Solution:
    def validPalindrome(self, s: str) -> bool:
        news = ""
        for x in s:
            if x.isalnum():
                news += x.lower()
        if len(news) == 2:
            return True
        print(news)
        l = 0
        r = len(news) - 1

        while l <= r:
            if news[l] != news[r]:
                return False
            l, r = + 1, - 1

        return True