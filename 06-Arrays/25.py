def occurs(number, array):
    for i in array:
        if i == number:
            return True
        else: 
            continue
    return False
n = int(input("Enter the number:"))


if occurs(n, [15, 38, 7, 23, 14]) == True:
    print("number", n, "appears in the array")
else: 
    print("number", n, "does not appear in the array")