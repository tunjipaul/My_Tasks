#task 5, modify tuple indirectly.
shopping_list = input("enter 3 items for your list: ").split()
list_convert_shopping_list = list(shopping_list)
print(list_convert_shopping_list)
added_items = input("add 2 more items: ").split()
print(added_items)
new_list = (list_convert_shopping_list + added_items)
print(new_list)
tupled_new_list = tuple(new_list)
print(tupled_new_list)
print("|".join(tupled_new_list))

