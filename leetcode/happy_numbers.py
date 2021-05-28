def happy_numbers(num):

    seen = {}  # to track the sum of square of digits 

    while num != 1:
        current = num
        sosod = 0  # sum of square of digits

        while current != 0:
            sosod += (current % 10) ** 2 #(current % 10)
            current //= 10
        
        if sosod in seen:  # if sum of square of digits gets repeated menas it forms cycle (can't be 1).

            seen[num] = sosod
            return False, seen # two smae sosod values indicates it is cyclic. So, not a happy number.

        else:  # if not then add it to the seen dictionary to track if any cycle form or not.
            seen[num] = sosod
            num = sosod

    # if we are out of the infinite loop and sosod is not in seen dictionary. It means it's a happy number.
    return True, seen


# Driver Code Starts
if __name__ == "__main__":

    num = int(input("Enter the number: "))

    print(happy_numbers(num))
