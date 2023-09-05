import heapq

n, k, x = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda tmp: tmp*-1, a))
heapq.heapify(a)
while 0 < k:
    pop = heapq.heappop(a)
    if pop == 0:
        break
    now = -pop
    use = now // x
    if use == 0:
        now = 0
        k -= 1
    else:
        now -= (min(k, use)*x)
        k -= min(k, use)
    heapq.heappush(a, -now)
print(abs(sum(a)))
