def calculateAmount(prices):

    total_cost = 0
    minimum = prices[0]
    discount = 0
    for i in range(len(prices)):
        price = prices[i]
        
        if i == 0:
            discount = 0
        else:
            # ye wala likhna hai niche wala
            discount = min(minimum, prices[i-1])
        
        
        if discount > price:
            price = 0
            discount = 0
        
        total_cost += (price - discount)
        #print(price, discount, total_cost)

    return total_cost


# Driver Code Starts
if __name__ == "__main__":
    n = int(input())
    prices = [int(i) for i in input().split()]
    
    print(calculateAmount(prices))
