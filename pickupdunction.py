customer_details = {}


print("Please enter pickup information ")

valid = False
while not valid:
    customer_details['name'] = input("please enter your name ")
    if customer_details['name'] != "":
        print (customer_details['name'])
        break 

    else:
        print("sorry this is left blank ")
valid = False
while not valid:
    customer_details['phone'] = input("please enter phone number ")
    if customer_details['phone'] != "":
        print (customer_details['phone'])
        break 

    else:
        print("sorry this is left blank ")


