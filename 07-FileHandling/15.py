f = open("30.txt")
count = 0
checker = 5
for line in f:
    print(line, end="")
    count+=1
    if count == checker:
        checker+=5
        if checker!=35:
            i = input("Press enter to continue ")