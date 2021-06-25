from time import time
def nobita(n, m):

    def isNobita(num):   
        while num // 10 != 0:
            n1 = num % 10
            
            num //= 10

            n2 = num % 10
            #print(f"n1: {n1}, n2: {n2}, num: {num}")
            if abs(n2 - n1) != 1:
                return False
        return True

    sum1 = 0
    t1 = time()
    for i in range(n, m + 1):
        
        if isNobita(i):
            sum1 += i
    t2 = time()
    print("time taken:", t2 - t1)
    return sum1
    

# Driver Code Starts
if __name__ == "__main__":
    a = input().split()
    n = int(a[0])
    m = int(a[1])
    print(nobita(n, m))
