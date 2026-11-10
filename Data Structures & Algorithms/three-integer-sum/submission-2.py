class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        triplets = []
        for a in range(len(nums) - 2):
            b = a + 1
            c = len(nums) - 1
            while b < c:
                if nums[a] + nums[b] + nums[c] == 0:
                    triplets.append([nums[a], nums[b], nums[c]])
                    b += 1
                elif nums[a] + nums[b] + nums[c] > 0:
                    c -= 1
                else:
                    b += 1
        ans = []
        triplets = set(map(str, triplets))
        for triplet in triplets:
            ans.append(eval(triplet))
        return ans