five = 0
two = 0
one = 0

amount = int(input(f"Enter the amount in PLN: "))
print(f"The amount of PLN {amount} in coins:")
while amount != 0:
    if amount >=5:
        five = amount//5
        amount = amount%5
        
    elif amount > 1:
        two = amount//2
        amount = amount%2
    else:
        one = amount//1
        amount = amount%1

print(f"5 zł - {five}")
print(f"2 zł - {two}")
print(f"1 zł - {one}")
