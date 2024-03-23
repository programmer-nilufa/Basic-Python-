order=int(input("Which item do you want? \n1.Half Kacchi \n2.Full Kacchi \nEnter here: "))

if order == 1:
    price = 150

    cold_drinks =int(input("Do you want cold drinks? \n1.Yes \n2.No \nEnter here: "))
    if cold_drinks == 1:
        price = price+50
        print("Your bill:",price)
    else:
        print("Your bill:",price)

elif order == 2:
    price = 250

    cold_drinks = int(input("Do you want cold drinks? \n1.Yes \n2.No \nEnter here: "))
    if cold_drinks == 1:
        price = price + 50
        print("Your bill:", price)
    else:
        print("Your bill:", price)
