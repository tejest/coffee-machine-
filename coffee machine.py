MENU = {
    "espresso":{
        "ingredients":{
            "water" : 50,
            "coffee":18
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }

}

profit = 0
resources ={
    "water":300,
    "milk":200,
    "coffee":100,
}

def is_resource_sufficient(order_ingredients):
    
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("no {item}")
            return False
    return True
def process_coins():
    print("please enter coins")
    total = int(input("how many q "))*0.25
    total += int(input("how many d"))*0.1
    total += int(input("how many n "))*0.05
    total += int(input("how many p "))*0.01
    return total

def is_transaction_successfull(money_recieved, drink_cost):
    if money_recieved>=drink_cost:
        change = round(money_recieved-drink_cost,2)
        print("change:{change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorru thats not enough")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is ur {drink_name}")


is_on=True

while is_on:
    choice = input("what would you like to have?(espresso,latte,cappuccino):)")
    if choice == "off":
        is_on = False
    elif  choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"]) 
        
        
        
       
    
    
    
    

    





























