class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l < 3:
            return 0

        left_max = [0] * l
        curr_left_max = 0
        for i in range(0, l):
            curr_left_max = max(curr_left_max, height[i])
            left_max[i] = curr_left_max

        right_max = [0] * l
        curr_right_max = 0
        for i in range(l - 1, -1, -1):
            curr_right_max = max(curr_right_max, height[i])
            right_max[i] = curr_right_max

        water = 0
        for i in range(0, l):
            minimum = min(left_max[i], right_max[i])
            water_over_curr = minimum - height[i]
            if water_over_curr > 0:
                water += water_over_curr 

        return water