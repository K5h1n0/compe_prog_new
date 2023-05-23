a,b,k = map(int,input().split())
if (a+b)-k <= 0:
    anst = 0
    ansa = 0
elif a-k <= 0:
    anst = 0
    ansa = b - abs(a-k)
else:
    anst = a-k
    ansa = b
print(anst,ansa)