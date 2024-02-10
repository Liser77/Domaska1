number = int(input("Введите пятизначное число: "))

a1 = number % 10
a2 = (number % 100) // 10
a3 = (number % 1000) // 100
a4 = (number % 10000) // 1000
a5 = number // 10000

result = (a2 ** a1) * a3
result /= (a5 - a4)

print(float(result))