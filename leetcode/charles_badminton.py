def badminton(n, arr):
    score = [0, 0]
    serve = 0
    for x in arr:
        if x == 'W' and serve == 0:

            score[0] += 1

            if score[0] >= score[1]:
                serve = 0
            else:
                serve = 1
            

        elif x == 'L' and serve == 0:
            score[1] += 1

            if score[0] >= score[1]:
                serve = 0
            else:
                serve = 1
        
        elif x == 'W' and serve == 1:
            score[1] += 1
            if score[0] >= score[1]:
                serve = 0
            else:
                serve = 1
            
        elif x == 'L' and serve == 1:
            
            score[0] += 1

            if score[0] >= score[1]:
                serve = 0
            else:
                serve = 1

    return score



# Driver Code Starts
if __name__ == "__main__":
    n = int(input())

    arr = input().split()
    
    a, b = badminton(n, arr)
    print(a, b)
