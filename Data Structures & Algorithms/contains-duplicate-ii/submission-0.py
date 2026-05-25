class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        num_map = {}

        for i, n in enumerate(nums):
            if abs(num_map.get(n, float("inf")) - i) <= k:
                return True
            num_map[n] = i

        return False