arr = [2, 3, 7, 5, 4]

#a
print(arr)
#b
print(len(arr))
#c
print(arr[0])
#d
print(arr[1])
print()
#e
print(arr[len(arr)-1])
print()
#f
print(arr[len(arr)-2])
print()
#g
print(arr[len(arr)//2])
print()
#h
print(arr[int(len(arr)/2)])
print()
#i
for i in arr:
    print(i, end=' ')
#j
print()
for i in range (len(arr)//2):
    print(arr[i], end=" ")
