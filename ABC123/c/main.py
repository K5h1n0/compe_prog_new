#解説AC
n = int(input())
l = []
for i in range(5):
    l.append(int(input()))
print(4 + (n + min(l)-1)//min(l))