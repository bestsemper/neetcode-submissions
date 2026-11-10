class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0
        left = [height[0]]
        right = [height[-1]]
        for i in range(1, len(height)):
            left.append(max(left[-1], height[i]))
            right.append(max(right[-1], height[len(height)-i-1]))
        right = list(reversed(right))
        for i, h in enumerate(height):
            totalArea += min(left[i], right[i]) - h
        return totalArea