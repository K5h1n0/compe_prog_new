#標準ライブラリ
import bisect

n,x = map(int,input().split())
a = list(map(int,input().split()))
print(bisect.bisect(a,x))

