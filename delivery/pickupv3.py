def delivery():
    print("Please enter delivery information")

    # Ask for name
    valid = False
    while not valid:
        customer_details['name'] = input("Please enter your name: ")
        if customer_details['name'] != "":
            print("Name:", customer_details['name'])
            break
        else:
            print("Sorry, this field cannot be left blank.")

    # Ask for phone number
    valid = False
    while not valid:
        customer_details['phone'] = input("Please enter your phone number: ")
        if customer_details['phone'] != "":
            print("Phone number:", customer_details['phone'])
            break
        else:
            print("Sorry, this field cannot be left blank.")

    # Check if it's delivery or pickup
    if choice == 1:  # Delivery
        # Ask for additional delivery details
        print("Please provide additional delivery details:")
        customer_details['Address'] = input("Address: ")
        customer_details['instructions'] = input("Delivery instructions: ")

        # Print delivery details
        print("Delivery details:")
        for key, value in customer_details.items():
            print(key.capitalize() + ":", value)
    else:  # Pickup
        print("Pickup details:")
        for key, value in customer_details.items():
            print(key.capitalize() + ":", value)


while True:
    try:
        choice = int(input("Please enter your choice (1 for Delivery, 2 for Pickup): "))
        if choice == 1:
            print("Delivery")
            break
        elif choice == 2:
            print("Pickup")
            break
        else:
            print("Wrong input, please enter 1 or 2.")
    except ValueError:
        print("This is not a valid number.")
        print("Please enter 1 or 2.")

customer_details = {}
delivery()
