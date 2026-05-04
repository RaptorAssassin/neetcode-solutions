class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # 1. Durchgang: Alles links vom Index i multiplizieren (Prefix)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # 2. Durchgang: Alles rechts vom Index i dazu multiplizieren (Suffix)
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res