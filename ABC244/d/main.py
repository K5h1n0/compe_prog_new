s1,s2,s3 = input().split()
t1,t2,t3 = input().split()
if s1 == t1 and s2 == t2 or s1 == t2 and s2 == t3 or s1 == t3 and s2 == t1:
    print("Yes")
else:
    print("No")