n = int(input())
n %= 30
s = ["1","2","3","4","5","6"]
for i in range(n):
    s[i%5],s[i%5+1] = s[i%5+1],s[i%5]
print(*s,sep="")