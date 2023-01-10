array = [2, 3, 2, 5, 8, 1, 9, 8]
unique = []

def f():
    print('Array:', array)
    for i in array:
        if array.count(i) == 1:
            unique.append(i)
    print('Unique elements:', unique)

f()