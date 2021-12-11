from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.followers = 0

    def follow(self, user):
        self.followers += 1
        user.followers += 1

    def increase_profit(self, profit):
        self.profit = profit


money_machine = MoneyMachine()
user1 = MoneyMachine()
user2 = MoneyMachine()
user1.follow(user2)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

turned_on = True
while turned_on:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}) ")
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    if user_input == "off":
        turned_on = False
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        user_drink = menu.find_drink(user_input)
        resources_sufficient = coffee_maker.is_resource_sufficient(user_drink)
        if resources_sufficient and money_machine.make_payment(user_drink.cost):
            coffee_maker.make_coffee(user_drink)
