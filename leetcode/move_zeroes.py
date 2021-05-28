def move_zeroes(nums):
    """
    [move all zeroes to the end of the array]
    # must be in-place without making a copy of the array.

    Args:
        nums ([int]): [array of numbers with zeroes and non-zeroes value]

    Returns:
        [nums]: [It will return nums array with all zeroes at the end]
    """

    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1

    for i in range(index, len(nums)):
        nums[i] = 0

    return nums


# Driver Code Starts
if __name__ == "__main__":
    
    nums = [int(num) for num in input("Enter the space separated array elements: ").split()]
    print(move_zeroes(nums))

    """
    Input :  nums = [1, 2, 0, 4, 3, 0, 5, 0]
    Output : nums = [1, 2, 4, 3, 5, 0, 0]

    Input : nums  = [1, 2, 0, 0, 0, 3, 6]
    Output : nums = [1, 2, 3, 6, 0, 0, 0]
    """
