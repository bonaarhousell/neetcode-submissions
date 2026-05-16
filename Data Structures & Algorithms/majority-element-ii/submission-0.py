class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 3:
            return []
        count = defaultdict(int)
        res = []
        for num in nums:
            count[num] += 1

        for n in count:
            if count[n] > n//3:
                res.append(n)
            
        return res