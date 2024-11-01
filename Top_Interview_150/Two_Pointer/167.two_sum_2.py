
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:

    # n = len(numbers)
    # solution = []
    # for i,a in enumerate(numbers[:-1]):
    #     for j,b in enumerate(numbers[i+1:]):
    #         print(a,b)
    #         if (a+b) == target:
    #             print('hhh')
    #             solution = [i,j]
    #             print(solution,i,j)
    # return(solution)
            

    n = len(numbers)
    i = 0
    j = n-1
    ans = [0] * 2
    

    while i < j:
        if numbers[i] + numbers[j] != target:
            j -= 1
            if j == i +1:
                i += 1
                j = n - 1
            print( 'i is' ,i, 'j is',j)
      
        
        else:
            ans [0] = i + 1
            ans [1] = j + 1
            break
            
    return ans
    
numbers = [2,7,11,15]
ans = twoSum(numbers, 9)

