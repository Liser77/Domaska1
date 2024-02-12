numbers = set()

numbers = input().split()
for number in numbers:
    if number in numbers:
        print("YES")
    else:
        print("NO")
        numbers.add(number)