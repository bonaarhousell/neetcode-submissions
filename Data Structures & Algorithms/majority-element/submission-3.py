class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = count

        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
            print(count)
        return res
            