x = int(input("enter first coordinate: "))
y = int(input("enter second coordinate: "))

if x > 0:
    if y > 0:
        quadrant = "first"
    else:
        quadrant = "fourth"
else:
    if y > 0:
        quadrant = "second"
    else:
        quadrant = "third"

print("Point P(", x, ",", y, ") is in the", quadrant, "quadrant of the coordinate system")