#task 2, tuple and input
user_name = input("names of your friends without commas: ") .split()
friends = tuple(user_name)
print(friends)
reverse_friends = friends[::-1]
print(reverse_friends)