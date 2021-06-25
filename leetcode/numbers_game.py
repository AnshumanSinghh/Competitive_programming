def f_x(n, arr):
    for i in range(n):
        f = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                break
            
        for k in range(j + 1, n):
            if arr[k] < arr[j]:
                f += 1
                break
        if f > 0:
            print(arr[k], end=" ")
        else:
            print(-1, end=" ")
            

# Driver Code Starts
if __name__ == "__main__":
    n = int(input())

    arr = [int(i) for i in input().split()]

    f_x(n, arr)