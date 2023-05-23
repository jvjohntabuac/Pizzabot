customer_details = {}
def delivery():
    print("Please enter pickup information")

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

    delivery_option = input("Please choose an option: delivery or pickup: ")

    if delivery_option.lower() == "delivery":
        # Ask for address
        print("Please provide additional delivery details:")
        customer_details['address'] = input("Address: ")
        customer_details['instructions'] = input("Delivery instructions: ")

    # Print delivery details
    print("Delivery details:")
    for key, value in customer_details.items():
        print(key.capitalize() + ":", value)
