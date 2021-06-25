"""
Runtime: 24 ms, faster than 93.79% of Python3 online submissions for First Bad Version.
"""

def isBadVersion(version):
    """
    Suppose isBadVersion is an API which returns whether the version is bad or not.
    """
    arr = [False, False, False, False, False, False, True, True, True, True]
    return arr[version - 1]


def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2
        #mid = left + (right - left) // 2

        if not isBadVersion(mid):
            left = mid + 1
        else:
            right = mid
    return left


# Driver Code Starts
if __name__ == "__main__":
    n = int(input())
    print(firstBadVersion(n))
