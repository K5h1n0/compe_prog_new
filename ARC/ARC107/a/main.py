# Σ 和の公式を用いる問題

a,b,c = map(int,input().split())
ans = (a*(a+1)//2)*(b*(b+1)//2)*(c*(c+1)//2)%998244353
print(ans)