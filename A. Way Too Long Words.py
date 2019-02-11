n = int(input())

for i in range(n):
    x = input()
    z = len(x)
    if z>10:
        print(x[0]+str(z-2)+x[-1])
    else:
        print(x)
