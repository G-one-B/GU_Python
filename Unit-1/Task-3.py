number = int(input('введите число:'))
if number == 1:
    print(number, 'процент' '0 процентов', '2 процента')
elif 1 < number < 5:
    print(number, 'процента', '0 процентов', '1 процент')
else:
    print(number, 'процентов', '1 процент', '2 процента')