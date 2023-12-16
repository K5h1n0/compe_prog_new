n = list(input())
if len(n) <= 3:
    print(*n,sep="")
    exit()
for i in range(3,len(n)):
    n[i] = "0"
print(*n,sep="")