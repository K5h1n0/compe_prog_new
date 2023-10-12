a, b = map(int, input().split())
if 0 < a and 0 < b:
    print("Positive")
if a <= 0 and 0 <= b:
    print("Zero")
if a < 0 and b < 0:
    if (a+b) % 2:
        print("Positive")
    else:
        print("Negative")
