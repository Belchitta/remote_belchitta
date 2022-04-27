price_list = [5, 10.7, 20.90, 21.05, 17.00, 15.99, 30.05, 31.99, 80.50, 50.50]
for price in price_list:
    print(f"{int(price)} руб. {int(price * 100 % 100):02} коп.", end=', ')


print('\nid price_list', id(price_list))
price_list.sort()
print('\nid price_list', id(price_list), price_list)


price_list_rev = sorted(price_list, reverse=True)
print('\nid price_list', id(price_list_rev), price_list_rev)

print(price_list[-5:])