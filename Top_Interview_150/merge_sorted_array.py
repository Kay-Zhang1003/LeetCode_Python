# Merger Sorted Array 
from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, last = m-1, n-1, m+n-1
    while j >= 0 and i>=0:
        if nums2[j] > nums1[i]:
            nums1[last] = nums2[j]
            j -= 1
        else:
            nums1[last] = nums1[i]
            i -= 1
        last -= 1

    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1,m,nums2,n)
    print(nums1)  