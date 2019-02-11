x = input()
li = ["+"]
nX = []
for i  in range(len(x)):
    if x[i] not in li:
        nX += x[i]

for j in range(len(nX)-1):
    for i in range(len(nX)-1):
        if nX[i]>nX[i+1]:
            temp = nX[i]
            nX[i] = nX[i+1]
            nX[i+1] = temp

for i in range(0,len(nX)):
    if i==0:
        print(nX[i],end='')
    else:
        print('+' + nX[i],end='')
            
