N = int(input())
num1 = [int(input()) for _ in range(N)]

num2 = num1[::-1]

for num in num2:
    print(num)