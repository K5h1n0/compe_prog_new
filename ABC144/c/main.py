n = int(input())
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        maximum = i
print(maximum+n//maximum-2)