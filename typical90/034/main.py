#まだわからん。

from collections import defaultdict

n,k = map(int,input().split())
a = list(map(int,input().split()))
d = defaultdict(int)
right = 0
ans = 0 # 区間の最大を保存する。
kinds = 0
for left in range(n):
    while right < n and kinds < k:
        d[a[right]] += 1
        right += 1
        kinds = len(d)
        print("whileループの中",kinds,d)
    """
    if left == right:
        right += 1
        continue
    """
    print(left,right," ",right-left)
    if ans < right - left:
        ans = right-left
        print("ansを更新しました！",ans)
    d[a[left]] -= 1
    if d[a[left]] == 0:
        print("削除します",d)
        kinds -= 1
        del d[a[left]]
print(ans)