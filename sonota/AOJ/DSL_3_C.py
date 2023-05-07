"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C&lang=ja
"""
n,q = map(int,input().split())
a = list(map(int,input().split()))
x = list(map(int,input().split()))
list_ans = []
for i in range(q):
    ans = 0
    right = 0
    measure = 0
    for left in range(n):
        while right < n and measure + a[right] <= x[i]:
            measure += a[right]
            right += 1
        ans += right-left
        if left == right:
            right += 1 # これを忘れない
            continue
        measure -= a[left]
    list_ans.append(ans)
print(*list_ans,sep="\n")