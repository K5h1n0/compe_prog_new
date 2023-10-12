n = int(input())
x = list(map(int,input().split()))
man =0
euc = 0
cheby = 0
for i in x:
    abso = abs(i)
    cheby = max(cheby,abso)
    man += abso
    euc += abso**2
print(man)
print(euc**0.5)
print(cheby)