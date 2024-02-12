def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_list(n):
    fact = factorial(n)
    factorial_lst = [fact]
    for i in range(n-1, 0, -1):
        fact //= i
        factorial_lst.append(fact)
    return factorial_lst

n = 3  # Пример входного числа
factorial2 = factorial_list(n)
print(factorial2)