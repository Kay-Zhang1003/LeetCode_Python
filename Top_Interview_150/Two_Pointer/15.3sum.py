from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = n-1
        
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif  nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    while l < r and nums[l] ==nums[l+1]:
                        l += 1
                    
                    while l < r and nums[r] ==nums[r+1]:
                        r += 1
                    
                    l +=1
                    r -=1
     

     
        return res
