def compare(array1, array2):
    print('Array1:', array1)
    print('Array2:', array2)
    if array1 == array2:
        print('Comparision: arrays are the same')
    else:
        print('Comparision: arrays are not the same')
    print()
compare(["water","book","sky"],["water","book","sky"])
compare([True,False],[True,False,True])
compare([5,3,1],[5,3,1])
compare([3,2,1],[3,2])