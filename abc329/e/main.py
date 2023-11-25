n,m = map(int,input().split())
s = input()
t = input()
flg = True
for i in list(set(list(t))):
    flg &= i in set(list(s))
flg &= s[0] == t[0]
flg &= s[-1] == t[-1]

l = [0]*(n+1)
i = 0
while i < n:
    if s[i] == t[0]:
        for j in range(m):
            if s[i+j] != t[j]:
                i += j
                break
            print("一致！",s[i+j],t[j])
        else:
            print("最後まで一致したよ")
            l[i] += 1
            l[i+m] -= 1
            i += m
        continue
    print("now",s[i])
    i += 1
print(l)
for i in range(1,len(l)):
    l[i] += l[i-1]
print(l)