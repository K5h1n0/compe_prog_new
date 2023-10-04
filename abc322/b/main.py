n, m = map(int, input().split())
s = input()
t = input()
pref = True
suff = True
for i in range(n):
    pref &= s[i] == t[i]

for i in range(n):
    suff &= s[i] == t[m-n+i]

if pref and suff:
    print(0)
elif pref:
    print(1)
elif suff:
    print(2)
else:
    print(3)
