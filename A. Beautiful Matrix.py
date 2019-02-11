mat = [[int(x) for x in input().split()] for i in range(5)]
m = 0
n = 0
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            m = i
            n = j
print(abs(m-2)+abs(n-2))

