
"""
INPUT: [0, 1, 2, 0, 1, 2, 0, 1]
OUTPUT: [0, 0, 0, 1, 1, 1, 2, 2]
it performs classification into elements less than, equal to, and greater than the pivot in a single
pass. This reduces runtime, at the cost of a trickier implementation. We do this by maintaining four
subarrays: bottom (elements less than pivot), middle (elements equal to pivot), unclassified, ar.d top
(elements greater than pivot). Initially, all elements areinunclassified. We iterate through elements
inunclassified, andmove elements into one of bottom,mi.ddle, andtop groups according to the relative
order between the incoming unclassified element and the pivot.
"""
def solveDutchProblem(A, pivot):
    print(A)
    smaller, equal, larger = 0, 0, len(A)
    value = A[pivot]

    while equal<larger:
        print(smaller, equal, larger)
        if A[equal]<value:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1

        elif A[equal] == value:
            equal +=1

        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
        
        print(A)
    return A 
        
        
print(solveDutchProblem([0,1,2,0,1,2,0,1], 1))