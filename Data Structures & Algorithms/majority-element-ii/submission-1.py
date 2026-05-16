class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)
        res = []
        for num in nums:
            count[num] += 1

        for n in count:
            if count[n] > n//3:
                res.append(n)
            
        return res