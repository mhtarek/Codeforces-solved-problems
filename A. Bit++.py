n = int(input())
sum = 0
for i in range(n):
    val = input()
    if val=="++X" or val=="X++":
        sum+=1
    else:
         sum-=1
print(sum)
