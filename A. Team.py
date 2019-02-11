n = int(input())

x = lambda:map(int,input().split())
c= 0
for i in range(n):
    a = list(x())
    sum=0
    for j in range(len(a)):
        
        if a[j] == 1:
            sum+=1
    if sum > 1:
        c+=1  
print(c)
