#Write a program that multiplies two nonnegative integers.

def add(a, b):
    """
    add two bits without using + operator.
    """
    running_sum, carryin, k, temp_a, temp_b = 0,0, 1, a, b
    while temp_a or temp_b:
        ak, bk = a & k, b & k
        print(ak, bk)
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        running_sum |= ak ^ bk ^ carryin
        carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1,
        temp_b >> 1)
        print(carryin, k, temp_a, temp_b)
    return running_sum | carryin

def multiply(x, y):
    """
    multiply two numbers without using * operators.
    """
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum,y)
        x, y = x>>1, y<<1
    return running_sum



print(multiply(2,5))