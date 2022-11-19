arr = [2, 3, 7, 5, 4]
print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[len(arr) -1])
print(arr[len(arr)-2])
print(arr[len(arr)//2])
print(arr[int(len(arr)/2)])

for i in arr:
    print(i, end=" ")

for i in range (len(arr)):
    print(arr[i], end=" ")