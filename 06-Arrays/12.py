array = [[2,5,4],[9,0,3]]
print(array)

columns = 0

for list in array:
    columns += len(list)

rows = len(array)
cols = len(array[0])
print(rows, cols)

cols = len(array[0][1])
print(array[1])
for i in array:
    print(1, end=" ")
    print()
for i in array:
    print(i[-1])