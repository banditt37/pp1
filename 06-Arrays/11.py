def f():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    selection = int(input('input the month number:'))
    selection -= 1
    print('given number month is', months[selection])

f()