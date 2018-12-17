"""

Given a number N. The task is to find the unit digit of factorial of given number N.

Example:
Input:
2
3
4

Output:
6
4
"""


def fact(n):
    if n>5:
        return 0
    # if n==1:
    #     return n
    # else:
    #     return n*(fact(n-1))%10
    a = 1
    for i in range(1,n+1):
        a = a*i%10
        print(a)
    return a

print(fact(22222222222222222222222222))