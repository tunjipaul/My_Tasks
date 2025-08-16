
#task 7, list manipulation

cities = ["ikeja", "new jersey", "new york", "california", "abeokuta"]
new_city = input(" i want to change the 3rd city: ")
cities[2] = new_city
cities.pop()
new_first_city = input("your new first city is: ")
cities.insert(0, new_first_city)
print(cities)