#a program that stores items and their prices in a dictionary.

#items should come from a list.

items_in_list = []
items_in_list.append("Fish")
items_in_list.append("Meat")
items_in_list.append("Milk")

price_of_fish = int(input("Fish Price is:$ "))
price_of_meat = int(input("Meat price is:$ "))
price_of_milk = int(input("Milk Price is:$ "))

market_list = {
    items_in_list[0] : price_of_fish,
    items_in_list[1] : price_of_meat,
    items_in_list[2] : price_of_milk
}
# print(market_list)

#display all items and prices

item_display = market_list.keys()
print(item_display)
price_display = market_list.values()
print(price_display), #is this even correct lol.

#update prices
item_update = input("Forgot something: ")
price_update = int(input("Price of Item: "))
market_list.update({item_update:price_update})

print(market_list)