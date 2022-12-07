def month(n):
    monthname = ''
    if n == 1:
        monthname = 'January'
    elif n == 2:
        monthname = 'February'
    elif n == 3:
        monthname = 'March'
    elif n == 4:
        monthname = 'April'
    elif n == 5:
        monthname = 'May'
    elif n == 6:
        monthname = 'June'
    elif n == 7:
        monthname = 'July'
    elif n == 8:
        monthname = 'August'
    elif n == 9:
        monthname = 'September'
    elif n == 10:
        monthname = 'October'
    elif n == 11:
        monthname = 'November'
    elif n == 12:
        monthname = 'December'
    return monthname

print(month(7))