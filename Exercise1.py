# Задача 1
# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# Пример:

# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

n = int(input('Input your number: '))
res = 0
while n / 10 != 0:
    if 123 % 10 !=0:
        temp = n % 10
        n //= 10
    res += temp

print(f'Your sum is {res}')