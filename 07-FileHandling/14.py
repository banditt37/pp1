f = open(input("Enter the name of the file: "))
counter = 0
for line in f:
    counter+=1
f.close()
print(f"File name: {f.name}")
print(f"Number of lines: {counter}")