def f():
    array = [[True,False],[True,True],[False,False]]
    print(array)
    for i in array:
        for x in i:
            if x == True:
                array.pop(x)
                array.insert(x, False)
            elif x == False:
                array.pop(x)
                array.insert(x, True)
    print(array)

f()