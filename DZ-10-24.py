my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list(arr, index):
    if index >= len(arr):
        print("Конец списка.")
    else:
        print(arr[index])
        print_list(arr, index + 1)

print_list(my_list, 0)