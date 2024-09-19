k = int(input())
n = int(input())
s = 0
for i in range(k, n+1):
    if i%2==0:
        s += i
print(s)