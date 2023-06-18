# インデックス管理で迷う
d = int(input())
n = int(input())
attend = [0]*(d+1)
for i in range(n):
    left,right = map(int,input().split())
    attend[left-1] += 1
    attend[right] -= 1
for i in range(1,len(attend)):
    attend[i] += attend[i-1]
print(*attend[:-1],sep="\n")