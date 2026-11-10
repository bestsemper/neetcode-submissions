class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        seq_len = 0
        for n in nums:
            if n - 1 not in hashset:
                tmp = 1
                nnext = n + 1
                while nnext in hashset:
                    nnext += 1
                    tmp += 1
                if tmp > seq_len:
                    seq_len = tmp
        return seq_len