#解説AC
#pizzaのどこに切れ込みが入っているか回すフェーズと、pizzaのそれぞれの角度を求めるフェーズの2段階に分けなきゃいけないのか。

n = int(input())
a = list(map(int,input().split()))
l = []
#0度と360度に切れ込みが入っている。
tmp = 0
l.append(tmp)
l.append(360)
#回すフェーズ
for i in range(len(a)):
    tmp += a[i]
    l.append(tmp%360)
l.sort()
#それぞれの角度を求めていくフェーズ
ans = []
for i in range(len(l)-1,0,-1):
    ans.append(l[i]-l[i-1])
print(max(ans))