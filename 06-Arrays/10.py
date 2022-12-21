def f():
    array = []
    i = 0
    while i < 11:
        array.append(i)
        i += 1

    even = 0
    odd = 0
    for i in array:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print('number of even valuees:', even, '\nnumber of odd values:', odd)

f()