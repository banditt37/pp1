humanyears = float(input(f"Enter the dog's age in human years: "))
dogyears = 0
if humanyears <=2:
    dogyears = humanyears * 10.5
elif humanyears > 2:
    humanyears = humanyears - 2
    dogyears = humanyears * 4 + 21
print(f"The dog's age in dog's years is {dogyears} years.")