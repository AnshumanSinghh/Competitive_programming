def land(arr):
    arr.sort(key=lambda x: x[1])
    d = {}
    for x in arr:
        d[x[1]] = x[0]
    values = list(d.keys())
    diff = [0, 0]
    for i in range(len(arr)-1):
        m = 0
        temp = (values[i + 1] - values[i])
        if m < temp:
            m = temp
            diff[0], diff[1] = values[i], values[i + 1]
    print(diff)
    ans =[]
    ans.append(d[diff[0]])
    ans.append(d[diff[1]])
    ans.sort()
    return ans


def land2(arr):
    arr.sort(key=lambda x: x[1])
    m = 0
    i1, i2 = -1, -1
    for i in range(len(arr) - 1):
        temp = arr[i + 1][1] - arr[i][1]
        if m < temp:
            m = temp
            i1, i2 = min(arr[i][0], arr[i + 1][0]), max(arr[i][0], arr[i + 1][0])
    return i1, i2
            

arr = [[3, 7], [1, 9], [5, 15], [4, 30]]

print(land(arr))
print(land2(arr))
    

    
