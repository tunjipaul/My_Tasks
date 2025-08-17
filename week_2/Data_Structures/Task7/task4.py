#unique members registration.

user_name = input("Enter three names OGA(use commas to separate names as you write): ").split(",")
#use split to separate them with commas, from lists then convert to sets and store in another variable.
set_user_name = set(user_name)

print(set_user_name)


name_length = ""
for i in set_user_name:
    print(f'{i.strip()}: {len(i)}')
    #haha, you caught me, i tried do this the manual way but sets cannot be keys in a dictionary. 
    #lol that would have been easier, i'm getting confused already. 
    #wait let me see.
# dict_number = dict(name_length)
# print(name_length) 
#ah this did not work, I guess that's where comprehension comes in. sigh i need to read more.
#.strio() removes unnecessary spaces after typing.

dict_members = {name : len(name) for name in set_user_name}
print(dict_members)


# {key_expression: value_expression for item in iterable if condition}

# dict_set_user_name = {user_name for name in set_user_name :  len(set_user_name)}
# print(dict_set_user_name)

