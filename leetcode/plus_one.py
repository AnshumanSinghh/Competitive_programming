"""
    [Faster than 87.06% python3 submissions]
"""
def plusOne(digits):

    n = len(digits)

    # we will traverse from last as most significant bit is the last one.
    for i in range(n - 1, -1, -1):

        # if I'th digit is less than 9 increse it by one return the digits array.
        if digits[i] < 9:

            digits[i] += 1

            return digits
        # if not then make it zero.
        digits[i] = 0

    # if we are here it means all the elements of digits are 9. So, make array of zeros
    # of length n and add [1] before this array of zeros. We are doing this because [9, 9]
    # becomes [1] + [0] * n  = [1] + [0, 0] (as length of [9, 9] is 2) = [1, 0, 0].
    digits = [1] + [0] * n

    return digits

# Driver Code Starts
if __name__ == "__main__":

    digits = [int(i) for i in input().split()]

    print(plusOne(digits))
    
