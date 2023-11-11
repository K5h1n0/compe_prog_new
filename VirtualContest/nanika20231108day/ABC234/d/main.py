import heapq

n,k = map(int,input().split())
p = list(map(int,input().split()))
q = p[0:k]
#print(q)
heapq.heapify(q) #元々あるリストをヒープ化