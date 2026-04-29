class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        count = 0
        res = count

        for num in nums:
            hashmap[num] += 1
            if count < hashmap[num]:
                res = num
                count = hashmap[num]
        return res
            