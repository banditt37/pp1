array = [-15, 8, -31, 47, -2, 19]

max = 0
min = array[0]

for i in range(0, len(array)):
    if array[i] > max:
        max = array[i]

    if array[i] < min:
        min = array[i]

print(max)
print(min)