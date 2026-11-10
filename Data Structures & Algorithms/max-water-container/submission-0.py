class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        maxArea = 0
        while a < b:
            tmp = (b - a) * min(heights[a], heights[b])
            if tmp > maxArea:
                maxArea = tmp
            if heights[a] < heights[b]:
                a += 1
            else:
                b -= 1
        return maxArea