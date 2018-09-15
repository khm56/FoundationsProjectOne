####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Coders Cafe"
signature_flavors = ["python", "java", "c++"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our menu: ")
    for key in menu:
        print("- %s (KD %s)" %(key,menu[key]))
        

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for flav in original_flavors:
        print("- %s" %(flav))

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here
    for flav in signature_flavors:
        print("- %s" %(flav))    


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    exist = False
    for flav2 in signature_flavors:
        if order==flav2:
            exist=True
            return True
    for flav1 in original_flavors:
        if order==flav1:
            exist=True
            return True          
    for key in menu:
        if order==key:
            exist=True
            return True            
    if exist == False:
        print("Item doesn't exist please review")
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    temp_in=""
    order_list = []
    # your code goes here!
    print("What is your order? (Enter the exact spelling of the item you want. Type'Exit' to end your order.")
    while True:
        temp_in = input()
        temp_in=str(temp_in.lower())
        if temp_in=="exit":
            break
        elif is_valid_order(temp_in)== True:
            order_list.append(temp_in)     
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total>=5:
        print("This order is eligible for credit card payment.")
    else:
        print("This order is not eligible for credit card payment.")
    
    
def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for item in order_list:
        for flav in original_flavors:
            if item == flav:
                total+= menu["original cupcake"]
        for flav2 in signature_flavors:
            if item == flav2:
                total+= menu["signature cupcake"]
        for key in menu:
            if item == key:
                total+= menu[key]
    print("That'll be KD %s" %(str(total)))
    accept_credit_card(total)
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for item in order_list:
        print("- %s" %(item))
    get_total_price(order_list)
    confirm=input("Confirm? (Y/N) ")
    confirm=str(confirm.upper())
    if confirm=="Y":
        print("Thank you for shopping at %s" %(cupcake_shop_name))
    elif confirm=="N":
        aor=input("Do you want to remove items? (Y/N) ")
        aor=str(aor.upper())
        if aor=="Y":
            print("What is the item you want to remove? please type it the exact same way as in your order list")
            item=input()
            item=str(item.lower())
            exi=False
            for order in order_list:
                if order==item:
                    exi=True
                    order_list.remove(item)
                    print_order(order_list)
            if exi==False:
                print("Your input does not exist in your order")
                print_order(order_list)
        elif aor=="N":
            print_order(order_list)
        else:
            print("Invalid Input")
            print_order(order_list)
    else:
        print("Invalid Input")
        print_order(order_list)



