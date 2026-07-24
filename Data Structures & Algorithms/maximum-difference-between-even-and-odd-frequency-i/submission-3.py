class Solution:
    def maxDifference(self, s: str) -> int:
        odEv = {}

        for x in s:
            if x not in odEv:
                odEv[x] = 1
            else:
                odEv[x] += 1

        odd, even = 0, 99999

        for val in odEv:
            if odEv[val] % 2 == 0:
                even = min(even, odEv[val]) 
            else:
                odd = max(odd, odEv[val])
                

        return odd - even
                
                    
