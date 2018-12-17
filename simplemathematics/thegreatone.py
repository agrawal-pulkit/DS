# code
"""
Given an array A of size N which consists of positive integers.
The task is to make the largest number K from array elements such that
every chosen array element has exactly 3 divisiors.

Example:
Input:
1
10
1 2 3 4 5 6 7 8 9 10

Output:
94
"""

def greatOne(a):
    num = []
    for i in a:
        count = 0
        for j in a:
            if i % j == 0:
                count += 1
            if count > 3:
                break
        if count == 3:
            num.append(i)

    return int(''.join(map(str, sorted(num, reverse=True))))


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().rstrip().split()))
        print(greatOne(a))