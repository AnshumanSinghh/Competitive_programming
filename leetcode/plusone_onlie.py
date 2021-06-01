"""
    [FOUND ONLINE]
    Works like magic because of bitwise negation operator(~): it takes the number n as binary number 
    and “flips” all bits 0 to 1 and 1 to 0 to obtain the complement binary number. For example, the 
    tilde operation ~1 becomes 0 and ~0 becomes 1 and ~101 becomes 010. In simple words ~0 --> -1,
    ~1 --> -2, ~5 --> -6 and so on.

    ~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. 
    This is the same as -x - 1.
"""

def plusOne(digits):
    for i in range(len(digits)):
        # if element at index ~i is < 9.
        if digits[~i] < 9:

            # then, increment it's value by 1
            digits[~i] += 1

            return digits

        # if element at index ~i is equal to 9, then make it zero
        digits[~i] = 0
    # if we are here means all elements are 9. So, make array of zeros(of length len(digits)) and add [1] before it.
    return [1] + [0] * len(digits)


# Driver Code Starts
if __name__ == "__main__":

    digits = [int(i) for i in input().split()]

    print(plusOne(digits))
