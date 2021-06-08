duration = int(input('введите количество секунд: '))
divisors = (3153600000, 31536000, 2592000, 86400, 3600, 60, 1)
placeholders = ('{} в', '{} г', '{} мес', '{} дн', '{} ч', '{} мин', '{} сек')
result = []
for d, p in zip(divisors, placeholders):
    tmp = duration // d
    if tmp != 0:
        result.append(p.format(tmp))
        duration -= d * tmp
print(' '.join(result))
