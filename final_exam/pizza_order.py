#!/usr/bin/env python3

import ast


class Pizza:
    def __init__(self, size, topping, price):
        self.size = size
        self.topping = topping
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.size > other.size

    def __lt__(self, other):
        return self.size < other.size


class StandardPizza(Pizza):
    def __init__(self, size, topping, price):
        super().__init__(size, topping, price)


class Order:
    def __init__(self, pizza_list):
        self.pizza_list = pizza_list

    def add_pizza(self, pizza_obj):
        self.pizza_list.append(pizza_obj)

    def get_total(self):
        total = 0
        for pizza in self.pizza_list:
            total += pizza.price
        return total


order_data = ast.literal_eval(input())
pizza_list = []

for pizza_data in order_data:
    if len(pizza_data) == 3:
        pizza = Pizza(pizza_data[0], pizza_data[1], pizza_data[2])
    elif len(pizza_data) == 2:
        pizza = StandardPizza(9, pizza_data[0], pizza_data[1])

    pizza_list.append(pizza)

order = Order(pizza_list)

print(order.get_total())

if pizza_list[0].price == pizza_list[1].price:
    print("same same")
else:
    print("different pizzas")

if pizza_list[0].size > pizza_list[1].size:
    print("big first")
else:
    print("big second")
