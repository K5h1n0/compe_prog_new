a,b,c,d = map(int,input().split())
flg = False
flg |= a+b==c
flg |= a+b==d
flg |= a+c==c
flg |= a+c==d
flg |= b+b==c
flg |= b+b==d
flg |= b+c==c
flg |= b+c==d
if flg:
    print("Yes")
else:
    print("No")