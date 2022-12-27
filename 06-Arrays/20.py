def star():
    arr = [12, 6, 4, 9, 10]
    x = str()
    i = 0
    for i in arr:
        for i in range(0, i, 1):
            x += '*'
        
        print(f'{len(x)}: {x}')
        x = ''

star()