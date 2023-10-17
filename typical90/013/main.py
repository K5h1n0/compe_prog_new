from collections import defaultdict
import heapq

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b,cost= map(int,input().split())
    d[a-1].append((cost,b-1))
    d[b-1].append((cost,a-1))

def dijk(start):
    #最短距離を記憶するリストと、訪問済みか判断するリストを、頂点n個分用意する。
    shortest_dist_list = [10**10] * n
    visited = [False] * n

    # 開始地点から開始地点への最短距離は0。開始地点は訪問済みにする。
    shortest_dist_list[start] = 0
    visited[start] = True

    q = []
    # BFSでは始点の頂点番号をdequeに入れれば良い。
    # しかしダイクストラ法では、始点からの辺のコストを辺の個数分入れる必要があるので、forループを書いている。
    for tuple in d[start]:
        heapq.heappush(q,tuple) #tupleの中身は(cost,v)
    while q:
        now_cost,now_v = heapq.heappop(q)
        if visited[now_v]: #qからはコストが最小の頂点が常に取り出されているはずなので、既に訪れた場所を再度訪れた時は最短でないことが確定している。
            continue
        shortest_dist_list[now_v] = now_cost
        visited[now_v] = True
        for tuple in d[now_v]:
            cost_next,v_next = tuple
            if visited[v_next]:
                continue
            heapq.heappush(q,(cost_next+shortest_dist_list[now_v],v_next))
    return shortest_dist_list #リストを返却

result = dijk(0)
print(result)
