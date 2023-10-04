# 累積和を2つ保持しておくやつ
# 鉄則本の累積Maxの問題と似ている？
n = int(input())
a = list(map(int, input().split()))
accum1 = [0]
total = sum(a)
accum2 = [total]
tmp = 0
for i in a:
    tmp += i
    accum1.append(tmp)
tmp = total
for i in a:
    tmp -= i
    accum2.append(tmp)
minimum = 10**10
for i in range(len(accum1)):
    minimum = min(minimum, abs(accum1[i] - accum2[i]))
print(minimum)
