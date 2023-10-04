s = input()
if int(s[-1]) in {2, 4, 5, 7, 9}:
    print("hon")
elif int(s[-1]) in {0, 1, 6, 8}:
    print("pon")
elif int(s[-1]) in {3}:
    print("bon")
