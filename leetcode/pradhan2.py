def divisble(s, t):
    n = len(s)
    p = len(t)
    new = ""
    for i in range(p):
        # new = t[:i + 1]
        new += t[i]
        
        rep1 = new * (n // (i + 1))
        rep2 = new * (p // (i + 1))

        if rep1 == s and rep2 == t:
            return len(new)

s = input()
t = input()

print(divisble(s, t))
