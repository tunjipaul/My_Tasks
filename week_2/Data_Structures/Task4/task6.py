#task 6, word analyzer.

user_input = input("input a word: ")
length_of_words = len(user_input)
check_upper = user_input.isupper()
check_lower = user_input.islower()
check_title = user_input.istitle()

reverse_word = user_input[::-1]


print(check_upper, check_lower, check_title, reverse_word)