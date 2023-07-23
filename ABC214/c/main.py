#DP
#解説
n = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
minimum_ind = t.index(min(t))
for i in range(n*2):
    #print(t[(minimum_ind+i)%n])
    t[(minimum_ind+i)%n] = min(t[(minimum_ind+i-1)%n]+s[(minimum_ind+i-1)%n],t[(minimum_ind+i)%n])
print(*t,sep="\n")