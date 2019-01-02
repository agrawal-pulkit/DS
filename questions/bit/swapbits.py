#swap bits at given position
"""
we first test if
the bits to be swapped differ. If they do not, the swap does not change the integer. If the bits are
diffurent, swapping them is the same as flipping their individual values.
"""
def swapbits(x, i, j):
    # Extract the i-tfi and j-th bjts, and see jf they differ.
    if (x >> i) & 1 != (x >> j) & 1:
    # i-th and j-th bits differ. We wi77 swap then by flipping their val.ues
    # Select the bits to flip with bit_nask. Since x^I = 0 when x = I and 1
    # when x = 0, we can perforn the flip X1R.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x