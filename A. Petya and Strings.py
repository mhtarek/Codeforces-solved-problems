x = lambda: input().lower()
a = x()
b = x()

if a==b:
    print(0)
    
for i in range(len(a)):
    if(a[i] > b[i]):
        print(1)
        break
    elif(a[i]<b[i]):
        print(-1)
        break
