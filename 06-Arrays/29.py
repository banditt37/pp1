#29.	Write a program that, for the given array of real numbers, displays the number of elements that are greater than the given value entered from the keyboard.
def f(k, n):
    array = []
    count = 0
    for i in range(0, n):
        array.append(int(input()))
    for i in array:
        if i > k:
            count+=1
    print("The number of elements that are greater than the given value is", count)
f(int(input("Enter the real number: ")), int(input("enter the number of elements in array: ")))