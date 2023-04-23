s = input()
t = input()
if s == "Y":
    print(chr(ord(t)+ord("A")-ord("a")))
else:
    print(t)