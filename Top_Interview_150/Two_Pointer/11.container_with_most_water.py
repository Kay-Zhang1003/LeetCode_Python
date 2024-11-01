from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1


        water =0

        while l < r:
            water = max(water,(r - l) * min(height[l],height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l +=1
        return water