class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0
        mp = {0 : 1}

        for num in nums:
            cursum += num
            diff = cursum - k
            
            res += mp.get(diff, 0)
            mp[cursum] = mp.get(cursum, 0) + 1

        return res