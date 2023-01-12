file = open("shopping.txt", "a")

while True:
    user_choice = input("Enter the name of product: ")
    if user_choice == "":
        break
    file.write(user_choice + "\n")

file.close()