"""
尺取法
https://www.youtube.com/watch?v=aqncsLxYt8s
n,x
l1 ... ln
x以下の区間の数で最大は幾つ
7 10
5 2 4 1 2 11 3 
"""
n,x = map(int,input().split())
l = list(map(int,input().split()))
right = 0
ans = 0
measure = 0 # メジャーの長さ
for left in range(n):
    while right < n and measure + l[right] <= x: #ここのwhileの条件に合わなくなるのは、今のメジャーに次区間l[right]を足すとxを超えることが予想される時。
        measure += l[right] # 右の人の移動に伴ってメジャーを進む分だけ出す
        right += 1
        # print(measure)
    ans = max(ans,right-left) # 半開区間で考えている？現在のrightのindexのところ
    if left == right:
        right += 1 # 同じ位置に来たら、左の人とともに、右の人も1つ移動する必要があるのでright+=1。
        continue #コンティニューをすることで、leftも右に1つズラすことができる。つまり、一緒に区間を一つ飛ばせる。
    measure -= l[left] # 左の人の移動に伴ってメジャーをその区間分だけ戻す。
    # print(measure)
print(ans)
# print(measure)のコメントアウトを外すと、しゃくとりしている様子が見れて面白い。