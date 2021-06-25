def minLength(sytemState, dist):

    def findi(s):
        find = []

        new = systemState[s + 1 :]
        for i in range(len(new)):
            if new[i] == 1:
                find.append(s + i + 1)
                break

        if len(find) == 0:
            find.append(-1)

        new2 = systemState[:s][::-1]
        for i in range(len(new2)):
            if new2[i] == 1:
                find.append(s - i - 1)
                break

        if len(find) == 1:
            find.append(-1)

        return find


    cost = []
    for i in range(len(systemState)):

        if systemState[i] != 1:
            find = findi(i)
            
            temp1 = dist[-1]
            temp2 = dist[-1]

            if find[0] != -1:
                temp1 = dist[find[0]] - dist[i]
            if find[1] != -1:
                temp2 = dist[i] - dist[find[1]]

            
            temp = min(temp1, temp2)
            cost.append(temp)
            sytemState[i] = 1
        
    print("Cost:", cost)
    res = sum(cost)
    
    if res == None:
        return 0
    return res


# Driver Code Starts
if __name__ == "__main__":
    systemState = []
    systemState_size = int(input())
    systemState = list(map(int, input().split()))

    dist = []
    dist_size = int(input())
    dist = list(map(int, input().split()))

    print(minLength(systemState, dist))

