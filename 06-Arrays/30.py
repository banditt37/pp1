#30.	Create a function minmax(array) that, for the given array of integers, returns a two-element array containing the smallest and largest values in the given array. 
array = []
n = int(input("enter the number of elements in array: "))
for i in range(0, n):
    array.append(int(input()))

def minmax(array):
    print("array:", array)
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    array2 = []
    array2.append(array[0])
    array2.append(array[-1])
    return array2

print(minmax(array))