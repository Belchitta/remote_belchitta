n = int(input('Введите процент '))
last_number = n % 10
if n == 1:
    print(n, 'процент')
elif last_number in range(2, 5) and n != 13:
    print(n, 'процента')
elif n in range(5, 21) or last_number == 0:
    print(n, 'процентов')
elif last_number == 1:
    print(n, 'процент')
else:
    print(n, 'процентов')
