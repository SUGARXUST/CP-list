from numpy import array


x, y = map(int, input().split())

arr = list(map(int, input().split()))
arr = [-i for i in arr]
arr.sort()
print(arr)

for i in range(y-1):
    arr[0] = -arr[0]
    print(arr)
print(sum(arr))
