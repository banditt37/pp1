array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]
array3 = [1, 3, 5, 6, 4, 2, 8, 7, 10, 9]

def bubblesort(array):
    print(array)
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print(array)


bubblesort(array1)
bubblesort(array2)
bubblesort(array3)