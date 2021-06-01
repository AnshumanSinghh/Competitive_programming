def maxProfit_1(prices: list[int]) -> int:
    """
    [Runtime]: 1084 ms
    Runtime beats 41.74 % of python3 submissions(as per leetcode).
    """
    minimum, su = prices[0], 0

    for i in range(len(prices) - 1):
        
        if prices[i] < prices[i + 1]:
            
            minimum = min(prices[i], minimum)

            su = max((prices[i + 1] - minimum), su)   
    return su



def maxProfit_2(prices: list[int]) -> int:
    """
    [Runtime]: 992 ms
    Runtime beats 68.56 % of python3 submissions(as per leetcode).
    """
    minimum = prices[0]
    maximum = 0
    ans = []
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            minimum = min(prices[i], minimum)
            maximum = prices[i+1]
            ans.append(maximum - minimum)
    if len(ans) == 0:
        return 0
    return max(ans)



def maxProfit_3(prices: list[int]) -> int:
    """
    [This is not mine method, above 2(1st & 2nd) are mine method]

    [Runtime]:1032 ms
    Runtime beats 57.60 % of python3 submissions(as per leetcode).
    """
    minimum, su = 999999, 0
    for i in range(len(prices)):
        if prices[i] < minimum:
            minimum = prices[i]
        else:
            su = max((prices[i] - minimum), su)
    return su

    

# Driver Code Starts
if __name__ == "__main__":
    prices = list(map(int, input("Enter the array elements: ").split()))

    print(maxProfit_1(prices))

    print(maxProfit_2(prices))

    print(maxProfit_3(prices))
