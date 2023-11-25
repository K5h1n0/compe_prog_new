n = int(input())
a = list(set(list(map(int,input().split()))))
a.remove(max(a))
print(max(a))