class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = nums[0]
        for n in nums[1:]:
            val = val ^ n
        return val