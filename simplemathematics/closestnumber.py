"""
Given two integers N and M.
The problem is to find the number closest to N and divisible by M.
If there are more than one such number, then output the one having
maximum absolute value.
Example:
Input:
2
13 4
-15 6
Output:
12
-18
"""


# code

def closestNumber(n, m):
    q = int(n / m)

    #first possible closest number
    n1 = m * q

    #second smallest closest number
    if n * m > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)

    #find the closest suitable number
    if abs(n - n1) < abs(n - n2):
        return n1

    return n2


if __name__ == "__main__":
    for _ in range(int(input())):
        a = list(map(int, input().rstrip().split()))
        print(closestNumber(a[0], a[1]))
