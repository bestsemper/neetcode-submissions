class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        right = [nums[-1]]
        for i in range(1, len(nums)):
            left.append(left[-1] * nums[i])
            right.append(right[-1] * nums[len(nums)-1-i])
        right = list(reversed(right))
        ans = [right[1]]
        for i in range(1, len(nums) - 1):
            ans.append(left[i-1] * right[i+1])
        ans.append(left[-2])
        return ans