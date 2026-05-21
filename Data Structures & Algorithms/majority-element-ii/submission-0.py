from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_requirement = len(nums) // 3
        counter = Counter(nums)
        return [element for element, count in counter.most_common() if count > majority_requirement]