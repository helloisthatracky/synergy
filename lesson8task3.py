m = int(input())
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

a.sort()

x = 0
j = n - 1
boats = 0

while x <= j:
    if a[x] + a[j] <= m:
        x += 1
    j -= 1
    boats += 1

print(boats)