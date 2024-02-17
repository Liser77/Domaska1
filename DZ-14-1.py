# вывод бинарного числа
'''
def binary(n):
    if n > 1:
        binary(n // 2)
    print(n % 2, end='')

binary(13)
'''
# Умножение
'''
def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b - 1)

result = multiply(5, 3)
print(result)
'''
# Возведение в степень
'''
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

result = power(2, 3)
print(result)
'''