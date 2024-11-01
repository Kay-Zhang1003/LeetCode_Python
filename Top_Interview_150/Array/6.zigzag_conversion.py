from typing import List
# def convert( s: str, numRows: int) -> str:
#     array = list(s)
#     n = len(array)
#     s = f = 0
#     ans = [''] * n
#     jumps = 2*numRows-2


#     for i in range(n):
#         if f < n:
#             ans [i] = array[f]  
#             f += jumps
#         elif s < numRows:
#             s +=1
#             f = s
            

#     return ''.join(ans)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        current_row = 0 
        
        for c in s :
            rows[current_row] += c
            if current_row == 0:
                direction =1
            if current_row == numRows-1:
                direction =-1
            current_row +=direction
            
        return ''.join(rows)

