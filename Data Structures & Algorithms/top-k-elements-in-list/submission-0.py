class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        groups = [[] for _ in range(len(nums) + 1)]
        for n in freq:
            groups[freq[n]].append(n)
        ans = []
        idx = len(nums)
        while k > 0:
            if len(groups[idx]) > 0:
                ans.extend(groups[idx])
                k -= len(groups[idx])
            idx -= 1
        return ans