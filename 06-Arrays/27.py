#27.	Write a program that displays the difference between the largest and smallest values in an array of integers. Sample result:
array = [5,1,9,6,1]
print("array:", array)
def sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print("result:", array[-1] - array[0])

sort(array)