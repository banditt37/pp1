pin = int("0805")

for i in range(3):
    pinn = int(input("Enter the PIN code: "))
    if pinn == pin:
       print("Correct")
       break 
    elif pinn != pin:
        print("Incorrect...")
    
if pinn!=pin:
   print("Sorry, your payment card has been blocked.")