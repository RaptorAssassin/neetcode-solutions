class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        smallest = float("inf")

        for price in prices:
            smallest = min(smallest, price)
            best = max(best, price - smallest)

        return best