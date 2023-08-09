s = list(input())
t = []
for i in range(len(s)):
    t.append(chr(ord(s[i])-32))
print("".join(t))


"""
s = list(input())
small = list("abcdefghijklmnopqrstuvwxyz")
large = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
t = []
for i in range(len(s)):
    t.append(large[small.index(s[i])])
print("".join(t))
"""