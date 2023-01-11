#26.	Write a program to find the second largest element in an array. Sample result:
#Array: [5,1,9,6,1]
#Result: 6


array = [5,1,9,6,1]
largest = []
x = 0
for i in array:
    if x < i:
        largest.append(i)
        x = i
print(largest[-2])