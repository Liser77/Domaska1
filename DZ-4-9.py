def count_divisors(x):
    divisors1 = 0
    i = 1
    while i * i <= x:
        if x % i == 0:
            divisors1 += 2 if i * i != x else 1
        i += 1
    return divisors1

x = int(input("Введите натуральное число X: "))

Delitel2 = count_divisors(x)

print("Колл-во натуральных делителей числа", x, ":", Delitel2)