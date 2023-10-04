from collections import defaultdict
n = int(input())
l = []
d = defaultdict(list)
for i in range(n-1):
    u, v, w = map(int, input().split())
