while True:
    try:
        delivery = int(input("please enter a valid option"))
        pickup = int(input("please enter a valid option"))
        if pickup >= 1 and delivery <= 2:
         if pickup == 1:
            print("Pickup")
            break
        elif delivery == 2:
            print ("Delivery")
            break
        else:
            print("wrong")
    except ValueError:
        print("this is not a valid number")
        print("please enter 1 or 2")
