class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maximum = 0

        for n in s:
            curr = 1
            if n - 1 not in s:
                c = 1
                while n + c in s:
                    curr += 1
                    c += 1
                maximum = max(maximum, curr)
            else:
                continue

        return maximum
