class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = s.replace(" ","-").strip("-")
        if not w:
            return 0
        s = "-" + w
        count = 0
        for w in s:
            if w == "-":
                count += 1

        res = 0
        print(s)
        for i in range(len(s)):
            if s[i] ==  "-":
                count -= 1

            if not count:
                res += 1

        return res - 1