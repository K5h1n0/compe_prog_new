n = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
first = t[:]
for i in range(2*n):
    first[i%n] = min(t[i%n],first[(i-1)%n]+s[(i-1)%n])
print(*first,sep="\n")