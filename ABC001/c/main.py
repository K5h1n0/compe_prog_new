deg,dis = map(int,input().split())
ans = ""
a = dis*10//6
if a%10 < 5:
    a = a//10
    a /= 10
else:
    a = a//10
    a += 1
    a /= 10
if 0 <= a <= 0.2:
    tmp = "0"
elif 0.3 <= a <= 1.5:
    tmp = "1"
elif 1.6 <= a <= 3.3:
    tmp = "2"
elif 3.4 <= a <= 5.4:
    tmp = "3"
elif 5.5 <= a <= 7.9:
    tmp = "4"
elif 8.0 <= a <= 10.7:
    tmp = "5"
elif 10.8 <= a <= 13.8:
    tmp = "6"
elif 13.9 <= a <= 17.1:
    tmp = "7"
elif 17.2 <= a <= 20.7:
    tmp = "8"
elif 20.8 <= a <= 24.4:
    tmp = "9"
elif 24.5 <= a <= 28.4:
    tmp = "10"
elif 28.5 <= a <= 32.6:
    tmp = "11"
elif 32.7 <= a:
    tmp = "12"
direction = [0,112.5,337.5,562.5,787.5,1012.5,1237.5,1462.5,1687.5,1912.5,2137.5,2362.5,2587.5,2812.5,3037.5,3262.5,3487.5,3600.0]
directions = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
for i in range(len(direction)-1):
    if direction[i] <= deg < direction[i+1]:
        ans += directions[i]
if tmp == "0":
    ans = "C 0"
else:
    ans = ans + " " + tmp
print(ans)