def f():
    array = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
    even = 0
    for i in array:
        for x in i:
            if x % 2 == 0:
                even += 1
    print(even)
f()