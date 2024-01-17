abc = list("ABCDE")
s = list(input())
t = list(input())
s.sort()
t.sort()
s = "".join(s)
t = "".join(t)
set1 = {"AB","BC","CD","DE","AE"}
set2 = {"AC","AD","BD","BE","CE"}
if s in set1 and t in set1 or s in set2 and t in set2:
    print("Yes")
else:
    print("No")