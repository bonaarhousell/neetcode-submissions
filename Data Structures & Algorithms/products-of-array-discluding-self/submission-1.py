class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k = len(nums) 
        prod = 1
        zero_cnt = 0
        for n in nums:
            if n:
                prod *= n
            else:
                zero_cnt += 1

        if zero_cnt > 1:
            return [0] * k
        print(zero_cnt, prod)
        res = [0] * k
        for i, c in enumerate(nums):
            if zero_cnt:
                if c:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod // c

        return res