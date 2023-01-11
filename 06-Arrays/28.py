array = [1,0,9,4,6]
array2 = [6,8,3,1,0,5,7]

def median(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array[int(n/2)])
median(array)
median(array2)