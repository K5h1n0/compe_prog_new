n = int(input())
l = list(map(int, input().split()))
l2 = range(min(l), max(l)+1)
print(sum(l2)-sum(l))
