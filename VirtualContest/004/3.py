h,w = map(int,input().split())
ans = 0
ans += max(0,(w - 1)*h)
ans += max(0,(h - 1)*w)
print(ans)