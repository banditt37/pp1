#26.	Write a program to find the second largest element in an array. Sample result:
array = [5,1,9,6,1]
print("array:", array)
def secondlargest(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print("result:", array[-2])

secondlargest(array)