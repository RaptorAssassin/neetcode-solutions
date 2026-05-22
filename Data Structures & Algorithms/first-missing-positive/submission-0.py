class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        seen = set()

        for num in nums:
            seen.add(num)
            if res == num:
                while res in seen:
                    res += 1
        
        return res
