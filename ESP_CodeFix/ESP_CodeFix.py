#############################################
#   ESP broken code - please fix            #
#                                           #
#   NAME:  Marlon Evans                     #
#                                           #
#   YOU MUST ADD ANNOTATION/COMMENTS        #
#   TO EXPLAIN WHAT YOU HAVE FIXED          #
#                                           #
############################################# 
# Item Name, Cost in a list
import datetime             ### fix 8: imported datetime ###

products = [['Cheese', 1], ["Potatoes",1.70], ["Carrots", 1.50], 
["Peas",1.10], ["Lettuce",0.80], ["Onions",1], ["Apples",0.70]]

customers = []

# discounts implemented in a dictionary
discounts = {
    'staff' : 5,
    'over25': 10,
}
#
#
#
def cast_input_to_int_safely(inp):
    try:
        return int(inp)
    except:
        return cast_input_to_int_safely(input("Please try again, number was not valid")) ### Fix 1: Adding missing bracket ####
#
#
#
def cast_input_to_float_safely(inp):
    try:
        return float(inp)
    except:
        return cast_input_to_float_safely(input("Please try again, decimal was not valid"))



def get_product(name):
    for product in products:
        if product[0].lower() == name.lower():                                                     ### fix 5 change 1 to 0 in [] ###
            return product
    return None


def sell_product():
    items = []
    while True:
        item = input("What item would you like to buy (type 'done' to continue to checkout):")
        if item == 'done':                                                                          ### fix 4: change != to == ###
            break
        else:
            product = get_product(item)
            if product is not None:
                item_added = product[:]
                item_added.append(cast_input_to_int_safely(input("Input how many of the item you would like to buy: "))) ### fix 6 corrected variable name by removing "to" ###
                items.append(item_added)
                print("Added item!")
                print("Current basket:" + ', '.join( ('{} ({})'.format(i[0], i[2]) for i in items)))
            else:
                print("Invalid product please type one of the following: " + ', '.join([i[0] for i in products]))
    customer_forename = input("What is the customers forename:").capitalize()
    customer_surname = input("What is the customers surname:").capitalize()
    customer_address = input("What is the customers address:")
    customer_postcode = input("What is the customers postcode:")
    customer_number = input("What is the customers phone number:")

    customers.append([customer_forename, customer_surname, customer_address, customer_postcode,
               customer_number])
    employee_discount = input("Is the customer an employee (makes them legible for employee discount)? (Y/N)").upper() == "Y" ### fix 11 changed from .lower to .upper ###
    print(items)
    subtotal = sum((i[1] * int(i[2]) for i in items))    ### fix 9: changed values to [1] and [2] ###
    print("\n-------RECEIPT-------")
    print("Customer: {} {}".format(customer_forename, customer_surname))                                            ### fix 7: fixed variable by adding "_" ###
    print("Items bought:\n" + '\n'.join( ('{} {} (TOTAL: £{:.2f})'.format(i[2], i[0], float(i[1]) * i[2]) for i in items)))
    print("Subtotal: £{:.2f}".format(subtotal))
    if employee_discount:
        print("Employee discount: -{}%".format(discounts.get('staff')))
        total = subtotal - (subtotal * (discounts.get('staff') / 100))
    else:
        total = subtotal
    if subtotal >= 25:                                     ### fix 10: changed from < to > ###
        print("Spend over £25 discount: -{}%".format(discounts.get('over25')))
        total -= subtotal * (discounts.get('over25') / 100)
    print("Total: £{:.2f}".format(total))            ### fix 12: changed from .4f to .2f ###

    str_items = ','.join( ('{}({})'.format(i[0], i[2]) for i in items))
    receipt = [datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"), customer_forename, customer_surname, customer_address, customer_postcode,
               customer_number, "£" + str(total), str_items]
    #
    #
    current_date_and_time = datetime. datetime. now()
    current_date_and_time_string = str(current_date_and_time) # convert to string
    extension = ".txt"
    file_name = current_date_and_time_string + extension
    newstr = file_name.replace(":", "")
    file_name = newstr[:17]
#
    with open (file_name, '+a') as f:
         f.write('\n'.join(receipt) + '\n')
#
# 


def mainmenu():
    print("\n------ Main Menu ------")
    print("+---------------------------------+")
    print(" option 1: Sell a product")
    print(" option 2: Exit")
    print("+---------------------------------+")
    option = input("which option? 1 or 2 ")
    while option != "1" and option != "2":                     #### Fix 2, or -> and###
        option = input("which option? 1 or 2 ")
    return option

#
####program flow starts here
#
while True:
    #
    choice = mainmenu()
    if choice == "1":
        sell_product()
    else:
      print("bye") # program ends
      break                                                  ### Fix 3 added a break###
        
  

