amount = int(input("Enter the amount in PLN: "))
print("The amount of PLN", amount, "in coins:\n")

coinsfive = 0
coinstwo = 0
coinsone = 0

while amount != 0:
    if amount >= 5:
        amount -= 5
        coinsfive += 1
    else:
        if a



print("5 zł - ", coinsfive)
print("2 zł - ", coinstwo)
print("1 zł - ", coinsone)