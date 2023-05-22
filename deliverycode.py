while True:
    try:
        delivery = int(input("Please enter choice for delivery: "))
        pickup = int(input("Please enter choice for pickup: "))
        if delivery == 1:
            print("Delivery")
            break
        elif pickup == 2:
            print("Pickup")
            break
        else:
            print("Wrong input, please enter 1 or 2.")
    except ValueError:
        print("This is not a valid number.")
        print("Please enter 1 or 2.")
   
