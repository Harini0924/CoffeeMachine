MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#intial resource values
money =0

# this function will see if the resource is available
def is_available(ingredients):
    for i in ingredients:
        if ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .25)
    return total

def istrancation_successful(money_received,drink_cost):

    if (money_received >= drink_cost):
        global money
        money += drink_cost
        change = round((money_received - drink_cost), 2)
        print(f"Here is you ${change} in change.")
        print(f"Here is your {ask}. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}.")






place_order= True
while (place_order ==True):
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if(ask=="off"):
        place_order=False
    elif(ask=="report"):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        user_drink = MENU[ask]
        if (is_available(user_drink["ingredients"])==True):
            payment = process_coins()
            if (istrancation_successful(payment, user_drink["cost"]) ==True):
                make_coffee(ask, user_drink["ingredients"])



