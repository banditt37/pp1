def f(x, y, value):
    if value >= x and value <= y:
        z = bool(1)
        return z
    else:
        z = bool(0)
        return z

print(f(10, 20, 35))