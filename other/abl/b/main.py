a,b,c,d = map(int,input().split())
ans = "No"
if a <= c and c <= b:
    ans = "Yes"
elif a <= d and d <= b:
    ans = "Yes"
elif c <= b and b <= d:
    ans = "Yes"
elif c <= a and a <= d:
    ans = "Yes"
print(ans)

#解説が天才では？
#https://blog.hamayanhamayan.com/entry/2020/09/27/012758