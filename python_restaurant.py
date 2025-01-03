menu={
    'Pizza': 40,
    'Burger': 60,
    'coffee': 70
}

print('Welocme to PYTHON restaurant')
print('Here is the menu\nPizza: Rs 40\nBurger: Rs 60\ncoffee: Rs 70')

order_1=input("Enter the name of your order- ")

total_cost=0

if order_1 in menu:
    total_cost+= menu[order_1]
    print("Your order has been added")

else:
    print("Please enter another order, as it is unavailable")

another_order= input("Do you want to add anytrhing else? (Yes/No)")

if another_order=='Yes':
    order_2= input("Please enter another order- ")
    if order_2 in menu:
        total_cost+= menu[order_2]
        print("Your order has been added")
    
    else:
        print("Your order is not available so summing up")

print(f"your total order price is Rs.{total_cost}")
   




