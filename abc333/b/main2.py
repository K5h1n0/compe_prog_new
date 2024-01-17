s = input()
t = input()

def f(s1,s2):
    abc = list("ABCDE")
    n1 = abc.index(s1)
    n2 = abc.index(s2)
    if n2 < n1:
        n1,n2 = n2,n1
    if n2 - n1 == 1 or n2 - n1 == 4:
        return True
    else:
        return False

if f(s[0],s[1]) == f(t[0],t[1]):
    print("Yes")
else:
    print("No")