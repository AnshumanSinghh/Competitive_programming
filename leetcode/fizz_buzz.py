def fizzBuzz_1(n: int) -> list[str]:
    """
    [Runtime]: 44 ms
    Runtime beats 52.44 % of python3 submissions.
    """
    arr = [0]*n
    for i in range(1, n + 1):
        if i % 15 == 0:
            arr[i-1] = "FizzBuzz"
        elif i % 3 == 0:
            arr[i-1] = "Fizz"
        elif i % 5 == 0:
            arr[i - 1] = "Buzz"
        else:
            arr[i-1] = str(i)
    return arr

def fizzBuzz_2(n: int) -> list[str]:
    """
    Runtime: 64 ms
    """
    arr = [0]*n
    for i in range(1, n + 1):
        d3 = (i % 3 == 0)
        d5 = (i % 5 == 0)
        if (d3 and d5):
            arr[i-1] = "FizzBuzz"
        elif d3:
            arr[i-1] = "Fizz"
        elif d5:
            arr[i-1] = "Buzz"
        else:
            arr[i-1] = str(i)
    return arr


def fizzBuzz_3(n: int) -> list[str]:
    """
    Runtime: 40 ms, faster than 79.94% of Python3 online submissions for Fizz Buzz.
    """
    arr = []
    for i in range(1, n + 1):
        d3 = (i % 3 == 0)
        d5 = (i % 5 == 0)
        if (d3 and d5):
            arr.append("FizzBuzz")
        elif d3:
            arr.append("Fizz")
        elif d5:
            arr.append("Buzz")
        else:
            arr.append(str(i))
    return arr


# Driver Code Starts
if __name__ == "__main__":

    n = int(input())

    print(fizzBuzz_1(n))

    print(fizzBuzz_2(n))

    print(fizzBuzz_3(n))