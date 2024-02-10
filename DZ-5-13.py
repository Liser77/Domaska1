m = int(input())
n = int(input())

weight = []
for i in range(n):
    weight.append(int(input()))

weight.sort()

boat = 0
left = 0
right = n - 1

while left <= right:
    if left == right:
        boat += 1
        break
    if weight[left] + weight[right] <= m:
        left += 1
    right -= 1
    boat += 1

print(boat)