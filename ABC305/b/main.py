p,q = input().split()
alphabet = ["A","B","C","D","E","F","G"]
l = [3,1,4,1,5,9]
if alphabet.index(p) > alphabet.index(q):
    pi = alphabet.index(q)
    qi = alphabet.index(p)
else:
    pi = alphabet.index(p)
    qi = alphabet.index(q)
ans = l[pi:qi]
print(sum(ans))