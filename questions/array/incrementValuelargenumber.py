
"""
Write a program which takes as input an array of digits encoding a nonnegative decimal integer
D and updates the array to represent the integer D + 1. For example, if the input is (1,2,9) then
you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
langua ge that has finite-precision arithmetic.
"""
def incrementAValue(A):
    print(A)
    A[-1] += 1
    for i in reversed(range(0, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    
    if A[0]== 10:
        A[1] = 1
        A.append(0)
    return A

print(incrementAValue([1,2,9]))