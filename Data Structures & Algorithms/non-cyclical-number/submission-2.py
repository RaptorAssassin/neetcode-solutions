class Solution:
    def isHappy(self, n: int) -> bool:
        sum_squares = n
        seen = set()

        while sum_squares not in seen:
            seen.add(sum_squares)
            sum_squares = sum([int(x)**2 for x in str(sum_squares)])
            if sum_squares == 1:
                return True

        return False