n,m = map(int,input().split())
list_gate = [0] * (n+1)
for i in range(m):
    l,r = map(int,input().split())
    list_gate[l-1] += 1
    list_gate[r] -= 1
tmp = 0
for i in range(len(list_gate)):
    tmp += list_gate[i]
    list_gate[i] = tmp
list_gate = list_gate[:-1]
print(list_gate.count(m))