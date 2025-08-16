#task 3
user_states = input("enter your preferred states: ").split()
state_tuple = tuple(user_states)
print(state_tuple)
print(state_tuple[0])
print(state_tuple[4])
print("lagos" in state_tuple)
state_tuple_length = len(state_tuple)
print(state_tuple_length)