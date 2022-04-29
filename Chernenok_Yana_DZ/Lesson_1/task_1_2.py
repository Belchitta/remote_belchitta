numbers_list = []
for i in range(1, 1001):
    if i % 2 != 0:
        numbers_list.append(i**3)
print(numbers_list)

sum_right_numbers = []
for number in numbers_list:
    i = number
    sum_number = 0
    while i > 0:
        digit = i % 10
        i = i // 10
        sum_number += digit
    if sum_number % 7 == 0:
        sum_number = 0
        sum_right_numbers.append(number)
print(sum_right_numbers)


result = 0
for i in sum_right_numbers:
    result += i
print(result)


numbers_list_add_17 = []
for i in numbers_list:
    i = i + 17
    numbers_list_add_17.append(i)
print(numbers_list_add_17)


sum_right_numbers_add_17 = []
for number in numbers_list_add_17:
    i = number
    sum_number = 0
    while i > 0:
        digit = i % 10
        i = i // 10
        sum_number += digit
    if sum_number % 7 == 0:
        sum_number = 0
        sum_right_numbers_add_17.append(number)
print(sum_right_numbers_add_17)


result_add_17 = 0
for i in sum_right_numbers_add_17:
    result_add_17 += i
print(result_add_17)
