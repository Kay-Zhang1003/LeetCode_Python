
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

def convert( s: str, numRows: int) -> str:
    n = len(s)
    rows = [''] * numRows
    current_row, direction = 0 , 0
    
    for c in s :
        rows[current_row] += c
        print(current_row)
        print(rows)
        if current_row == 0:
            current_row +=1
        if current_row == numRows-1:
            current_row -=1
    
    return ''.join(rows)

s =convert('PAHNAPLSIIGYIR',3)
print(s)