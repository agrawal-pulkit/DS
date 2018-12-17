"""
Given a number N. Find a number K such that product of digits of K must be equal to N.
Note : K must be as small as possible.
Example:
Input:
2
12
5

Output:
26
5
"""

def number(n):
    s = []
    for i in range(9, 1, -1):
        while (n % i == 0):
            s.append(i)
            n = n / i
    if n != 1:
        return -1

    k = 0
    while s:
        k = k * 10 + s.pop()

    return k


if __name__ == "__main__":
    for _ in range(int(input())):
        print(number(int(input())))