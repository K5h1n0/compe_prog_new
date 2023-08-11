import heapq

print("元のl")
l = [6,3,5,8,7,2]
print("l =",l)

# heapq.heapify()で、元からあるリストを優先度付きキューに変換。
print("heap化したl")
heapq.heapify(l)
print("l =",l)

#リストの左端（インデックス0）に常に最小値が来るようになっている。
print("l[0] =",l[0])

# heapq.heappop()をすると、最小値が取得できる。
print("heappopしてminimumに入れる")
minimum = heapq.heappop(l)
print("minimum =",minimum)

# 値を追加したい時はheapq.heappush(追加したいリスト,追加したい値)
print("lに1をheappush")
heapq.heappush(l,1)
print("l =",l)
print("l[0] =",l[0])

print("lに10をheappush")
heapq.heappush(l,10)
print("l =",l)
print("l[0] =",l[0])