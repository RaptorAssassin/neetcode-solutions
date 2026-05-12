class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets_set = set()

        map = defaultdict(list)
        for i, n in enumerate(nums):
            map[n].append(i)

        for i in range(len(nums)):
            val = nums[i]

            for j in range(i + 1, len(nums)):
                complement = 0 - (val + nums[j])

                if complement in map and map[complement] and any(k != i and k != j for k in map[complement]):
                    triple = sorted([nums[i], nums[j], complement])
                    triplets_set.add(tuple(triple))

        return [list(t) for t in triplets_set]