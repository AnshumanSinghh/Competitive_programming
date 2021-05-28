def single_number1(nums):
    """
    Time complexity : O(n^2).
    Space complexity : o(n).
    """
    li = []  # list which will not store any duplictae elements.

    for x in nums:

        # uf the number is already present in the li the remove it.
        if x in li:
            li.remove(x)

        # if the number is not in the li then add it.
        else:
            li.append(x)

    # the last remaining element will be the only non-duplicate element.
    print(li[0])




# 2nd approach using dictionary [more efficient]

def single_number2(nums):
    """
    Time complexity : O(n⋅1) = O(n).
    Space complexity : O(n).
    """
    dictionary = {}  # create empty dictionary [key = elements of array nums and
                     # value = frequency / count of duplicate element]

    for i in range(len(nums)):
        
        # if element is present in the dictionary then increse it's count by 1.
        if nums[i] in dictionary:
            dictionary[nums[i]] += 1

        # if not present then mark it's count as 1.
        else:
            dictionary[nums[i]] = 1
    
    # now traverse the dictionary and print the element whose count is 1.
    for i in dictionary:
        if dictionary[i] == 1:
            print(i)
            break


# 3rd approach using XOR operation.
"""
logic: 
XOR of same number is zero Ex: 1 ^ 1 = 0) and 
XOR of 0 with any number is that number itself (Ex: 0 ^ 8 = 8)
"""
def single_number3(nums):
    """
    Time complexity : O(n).
    Space complexity : O(1).
    """
    a = 0
    for i in nums:
        a ^= i
    return a

nums = [int(num) for num in input("Enter the space separated array elements: ").split()]

single_number1(nums)

single_number2(nums)

print(single_number3(nums))

