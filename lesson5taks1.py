number = int(input())
if number == 0:
    print('нулевое число')
elif number % 2 == 0:
    if number > 0:
        print('положительное четное число')
    else:
        print('положительное нечетное число')
else:
    if number > 0:
        print('положительное нечетное число')
    else:
        print('отрицательное нечетное число')