x = int(input())
count = 2
for i in range(2,x):
    if x % i == 0:
        count +=1
print(count)