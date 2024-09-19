s = 0
for i in range(int(1e6)):
    num6 = int(i%10)
    num5 = int((i%100)//10)
    num4 = int((i%1000)//100)
    num3 = int((i//1e3)%10)
    num2 = int((i//1e4)%10)
    num1 = int((i//1e5)%10)
    x1 = num1 + num2 + num3
    x2 = num4 + num5 + num6
    if x1 == 13  and x2 == 13:
        s += 1
print(s)