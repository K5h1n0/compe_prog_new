l = int(input())
n = int(input())
m = int(input())
n += m//25
m %= 25
l += n//4
n %= 4
l %= 10
print(l+n+m)