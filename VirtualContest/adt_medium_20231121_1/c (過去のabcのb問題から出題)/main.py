p = list(map(int,input().split()))
s = ""
for i in p:
    s += chr(ord("a")-1+i)
print(s)