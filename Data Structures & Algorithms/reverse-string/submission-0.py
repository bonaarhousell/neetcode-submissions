class Solution:
    def reverseString(self, s: List[str]) -> None:
        tmp = []
        for i in range(len(s)-1, -1, -1):
            tmp.append(s[i])
        for i in range(len(s)):

            print(tmp[i])
            s[i] = tmp[i]
 