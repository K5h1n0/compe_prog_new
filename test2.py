import time

n, x = map(int, input().split())
A = list(map(int,input().split()))
# n * x の２次元配列を作成
dp = [[0]*(x + 1) for _ in range(n)]

# この動的計画法では、おもりが何も無い時について考えていない。
# 1番目のおもり
dp[0][0] = 1
if A[0] <= x: # もし1番目のおもりが、判定したいところより小さければ書き込む。
    dp[0][A[0]] = 1

# 2番目以降のおもり 
for i in range(1,n):
    for j in range(x + 1):
        ref = dp[i - 1][j]  # 参照するのは今forで走査している行の、一個上のマスを見ている。
        if A[i] > j: # 今いる場所jが、入れるおもりの重さより小さい時は、上のマスをそのままコピーするだけで良い。
            dp[i][j] = ref
        else:
            # 今いる場所jがいまの重りの重さを超えたタイミングで初めて、ひとつ上のマスのj-おもりの重さを参照する事ができる。
            ref_back = dp[i - 1][j - A[i]]
            dp[i][j] = ref or ref_back # orってこういう使い方できるのか。1つ上のマスか、1つ上の[今のマス-今のおもりの重さのマス]が1ならば、そのマスに1を書く。
        """
        # time.sleep(0.001)
        print("----------------")
        for k in range(len(dp)):
            print(A[k],dp[k])
        """
print("yes" if dp[n-1][x] else "no")