n = int(input())
l = []
cardset = set()
flg = True
card = set(["H","D","C","S"])
num = set(["A","2","3","4","5","6","7","8","9","T","J","Q","K"])
for i in range(n):
    inp = input()
    cardset.add(inp)
    flg &= inp[0] in card and inp[1] in num
flg &= n == len(cardset)
if flg:
    print("Yes")
else:
    print("No")