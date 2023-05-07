n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
right = 0
for left in range(n):
    # print("今のleft",left)
    while right < n and a[right] - a[left] < x: # ==は含まないのがポイント。a[right]-a[left]がxより小さい時だけ、右端が右に右にズレていく。
        right += 1
        # print("1つ右へ。今のrightは",right)
    if right < n and a[right] - a[left] == x: # もし右端と左端の差がxなら発見できたので終了。
        print("Yes")
        exit()
    # 右端と左端の差がxより大きかったら、rightはそのままに、for文が回ることでleftが右にズレて行き、差が縮まっていく。
    # right==n、つまり、右端がlen(a)の一つ右に出てしまう、つまり、それ以降はa[right]-a[left]がどう頑張ってもxにならないのでbreak。
    if right == n:
        break
print("No")