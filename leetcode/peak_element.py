def findPeakElement_1(nums: list[int]) -> int:
    """
    63 / 63 test cases passed.
	Status: Accepted
    Runtime: 56 ms
    Memory Usage: 14.5 MB
    """
    n = len(nums)
    m = nums[0]
    for i in range(n - 2):

        # if array is sorted in decresing order, peak wll be at 0 index.
        if m > nums[i + 1] > nums[i + 2]:
            if i + 2 == n - 1:
                return 0

        # if array is sorted in increasing order, peak will be at last index.
        elif m < nums[i + 1] < nums[i + 2]:
            if i + 2 == n - 1:
                return i + 2

        # if not sorted then element must be in between of 0 and n-1 index.
        elif nums[i] < nums[i + 1] > nums[i + 2]:
            return i + 1

    # if all above conditions are false then it means nums is arranged in zig-zag
    # manner such that peak element is either at 0 index or at last index, as we
    # already checked all of the indexes between 0 ans last. So, return 0 if 0 index
    # element is greater or equal to last element, return n-1 otherwise.
    if nums[0] >= nums[n - 1]:
        return 0
    return n - 1

# Modified Version of 1st:
def findPeakElement_2(nums: list[int]) -> int:
    """
    Runtime: 52 ms, faster than 10.43% of Python3 online submissions for Find Peak Element.
    """
    n = len(nums)
    for i in range(n - 2):

        # check for peak elements between ) to n-1 index. If found return i+1 (index of peak element).
        if nums[i] < nums[i + 1] > nums[i + 2]:
            return i + 1

    # if peak is not between 0 and n-1 index. Then, it must be at 0 or n-1 index. So, return the
    # index of greates element among first and last element.
    if nums[0] >= nums[n - 1]:
        return 0
    return n - 1

# Binary Search Approach: O n(logn)
def findPeakElement_3(nums: list[int]) -> int:
    """
    Runtime: 44 ms, faster than 73.76% of Python3 online submissions for Find Peak Element.
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        # mid = left + (right - left) // 2
        mid = (right + left) // 2
        print("mid:", mid)
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid 
    return left
    


# Driver Code Starts
if __name__ == "__main__":
    nums = [int(i) for i in input().split()]
    print(findPeakElement_1(nums))
    print(findPeakElement_2(nums))
    print(findPeakElement_3(nums))
