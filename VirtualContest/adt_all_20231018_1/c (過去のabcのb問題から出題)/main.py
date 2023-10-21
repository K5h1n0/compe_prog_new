s = set(["ABC","ARC","AGC","AHC"])
s2 = set()
for i in range(3):
    s2.add(input())
print(*s ^ s2)