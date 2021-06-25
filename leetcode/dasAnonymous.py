def game_sort(n, arr):
    d = {}
    mid = n // 2
    for x in arr:
        d[x] = str(x)[mid]
    d1 = sorted(d.items())
    d1.sort(key= lambda x : x[1])
    ans = [x[0] for x in d1]
    return ans


n = int(input("n: "))

arr = [int(i) for i in input().split()]

print(game_sort(n, arr))

# Input: 10201 30215 90051 36103 92315

# Output: [90051, 36103, 10201, 30215, 92315] sorted array based on middle digit.
