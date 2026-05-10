class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}

        l = 0 
        res = 0
        maxV = 0

        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            maxV = max(maxV, mp[s[r]])

            while (r - l + 1) - maxV > k:
                mp[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res