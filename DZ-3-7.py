def a1(X, A, B):
    if X <= A + B:
        return 2
    elif X > A and X <= B:
        return "Ivan"
    elif X > B and X <= A:
        return "Mike"
    elif X > A + B and (X <= A or X <= B):
        return 1
    else:
        return 0

X = int(input("Минимальную сумму инвестиций: "))
A = int(input("Денег у Майка? "))
B = int(input("Денег у Ивана? "))

result = a1(X, A, B)
print(result)