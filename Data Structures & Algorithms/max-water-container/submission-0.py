class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) - 1
        res = 0

        res = heights[n] * heights[n]   
        return res