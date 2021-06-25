n = int(input())

chola_ne = []
chera_nw = []
pallava_sw = []
pandya_se = []
renounce = []

for _ in range(n):
    name = input()
    x = int(input())
    y = int(input())

    # 1st quadtrant means North-east.
    if x > 0 and y > 0:
        chola_ne.append(name)
    
    # 2nd quadrant means Nort-west.
    elif x < 0 and y > 0:
        chera_nw.append(name)

    # 3rd quadrant means South-west.
    elif x < 0 and y < 0:
        pallava_sw.append(name)
    
    # 4th quadrant means South-east.
    elif x > 0 and y < 0:
        pandya_se.append(name)

    # from no wehere
    else:
        renounce.append(name)
print("Output:\n")
print("chola")
print(chola_ne)

print("chera")
print(chera_nw)

print("pallava")
print(pallava_sw)

print("pandya")
print(pandya_se)

print("renounce")
print(renounce)
