#29.	Write a program that, for the given array of real numbers, displays the number of elements that are greater than the given value entered from the keyboard.
array = []
count = 0
k = int(input("Enter the real number: "))
n = int(input("enter the number of elements in array: "))
for i in range(0, n):
    array.append(int(input()))
for i in array:
    if i > k:
        count+=1
print("The number of elements that are greater than the given value is", count)