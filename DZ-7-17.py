list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

numbers = list1.intersection(list2)
print(len(numbers))