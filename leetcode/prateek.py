def ascending_order(n, arr):
    ans = []
    for i in range(n - 1):
        if (arr[i] < arr[i + 1]):
            ans.append(arr[i])
    if arr[i -1] < arr[i]:
        ans.append(arr[i])
    return n - len(ans)

# Driver Code Starts
if __name__ == "__main__":
    n = int(input())

    arr = [int(i) for i in input().split()]

    print(ascending_order(n, arr))