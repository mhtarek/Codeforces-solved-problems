n,m,a = map(int,input().split())

l = int(n/a)
w = int(m/a)

if  n%a!=0:
    l+=1
if m%a!=0:
    w+=1

print(l*w)
