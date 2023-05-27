def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

a,b,k = map(int,input().split())
print(fact(a)*fact(b)//fact(b))