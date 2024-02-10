def ar1(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    arr2 = [arr[-1]] + [arr[i] for i in range(n-1)]
    
    return arr2

N = int(input())
nums = list(map(int, input().split()))

ar1 = ar1(nums)

for num in ar1:
    print(num, end=" ")