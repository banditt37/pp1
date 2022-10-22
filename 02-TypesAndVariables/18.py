import math
a = int(input("lenght of first side: "))
b = int(input("lenght of second side: "))
c = int(input("lenght of third side: "))
s = ((a+b+c)/2)
h = (math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("area of the triangle:", h)