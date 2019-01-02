#find a parity of a bit of a large 64-bit number


"""
This is brute force approach will take time.
The time complexity isO(n), where n is the word size.
"""
def parity1(x):
    result = 0
    while x:
        result  ^= x & 1
        print(result)
        print("x: ", x)
        x >>= 1
    return result


def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drops the -lowest set bit of x
        print(result)
        print("x: ", x)
    return result

"""
best approach with O(logn)
The parity of (11010111) is the stune as the parity
of (1101) XORed with (0111), i.e., of (1010). 
This in tum is the same as the parity of (10) XORed with
(10), i.e., of (00). The final result is the XOR of (0) 
with (0), i.e.,0, Note that the first XOR yields
(11011010), and only the last 4 bits are relevant going forward.
The second XOR yields (11101100),
and only the last 2 bits are relevant. 
The third XOR yields (10011010). The last bit is the result, and
to extract it we have to bitwise-AND with (00000001).
"""
def parity2(x):
    x ^= x >> 32
    x^=x>>16
    x^=x>>8
    x ^= x >> 4
    x^=x>>2
    x^=x>>1
    return x & 0x1

print(parity2(115))