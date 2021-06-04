# Recursive approach
def isPowerOfTwo_1(n: int) -> bool:
    """
    1108 / 1108 test cases passed.
	Status: Accepted
    Runtime: 48 ms
    Memory Usage: 14.3 MB
    """
    if n == 1 or n == 2:
        return True

    if n % 2 != 0 or n == 0:
        return False

    return isPowerOfTwo_1(n/2)


def isPowerOfTwo_2(n: int) -> bool:
    """
    1108 / 1108 test cases passed.
	Status: Accepted
    Runtime: 40 ms
    Memory Usage: 14.3 MB
    """
    x = 0
    while x < n:
        if 2 ** x == n:
            return True
        elif 2 ** x > n:
            return False
        x += 1

# Driver Code Starts
if __name__ == "__main__":
    
    n = int(input())

    print(isPowerOfTwo_1(n))

    print(isPowerOfTwo_1(n))
