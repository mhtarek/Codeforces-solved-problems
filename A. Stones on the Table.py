n = int(input())
s = input()
nei=0
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        nei+=1
        
print(nei)
