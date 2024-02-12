N = int(input())
numbers = list(map(int, input().split()))

numbers2 = len(set(numbers))
print(numbers2)