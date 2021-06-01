"""
    Question description: You are given n(size fo array) and array elements. Original product should be 
    from smallest element of array to the largest element of the array. But user gives less elments than that.
    So, you have to find how many products are missing.

    Input: n = 4
           arr = [4, 2, 3, 9]

    Output: 4
    Expalanation: as product should be from 2 to 9 i.e, [2, 3, 4, 5, 6, 7, 8, 9]. It has total 8 elements
    but user provvided only 4. So, 8 - 4  = 4 is missing (namely [5, 6, 7, 8]).
"""

given_n = int(input("Enter the value of N: "))

nums = []

for _ in range(given_n):
    nums.append(int(input("Enter the number: ")))

nums.sort()

original_n = nums[-1] - nums[0] + 1

print(original_n - given_n)
