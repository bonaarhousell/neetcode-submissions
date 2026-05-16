class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        res = 0
        sell = 0
        buy = 0
        thus = 0
        mp = defaultdict()
        for i, p in enumerate(prices):
            mp[p] = mp.get(p, 0) + i

        print(mp)
        for r in range(len(prices)):
            sell = max(sell, prices[r])
            while prices[r] < prices[l]:
                thus += 1
                if thus == len(prices) -1 :
                    return 0
                l = r
                buy = prices[r]
                if mp[sell] < mp[buy]:
                    sell = 0
            res = sell - buy

        return res