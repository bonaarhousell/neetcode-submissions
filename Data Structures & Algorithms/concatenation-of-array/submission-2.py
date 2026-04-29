class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                print (n)
                ans.append(n)

        return ans