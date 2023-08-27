import heapq

n = int(input())
a = list(set(map(int, input().split())))
a = list(map(lambda x: x*-1, a))
heapq.heapify(a)
print(a)
