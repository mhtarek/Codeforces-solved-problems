i = lambda:map(int,input().split())

n,k  = i()

a = list(i())
count = 0
for x in a:
    if x >= a[k-1] and x>0:
        count+=1
        
print(count)
