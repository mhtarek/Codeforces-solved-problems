n = input()
n = n.lower()
x = ["a","e","i","o","u","y"]
l = ""
for i in range(len(n)):
    if n[i] not in x:
        l +='.'
        l += n[i]
print(l)


