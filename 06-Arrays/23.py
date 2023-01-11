array = [4,36,12,28,9,44,5]
array2 = [5,1,36]
array3 = [1, 3, 5, 6, 4, 2, 8, 7, 10, 9]
def bubblesort(array):
    print("unsorted array:", array)
    n = len(array)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print("sorted array:", array)
bubblesort(array)
bubblesort(array2)
bubblesort(array3)