#store inventory update.

store = {
    "book": 10,
    "pen" : 20,
    "bag" : 5
}
user_input = input("What do you want to buy? ").lower()
user_price = int(input("What's the price? "))

updated_store = store.copy()

updated_store[user_input] -= user_price

print(f"Before Purchase: {store}")
print(f"After Purchase: {updated_store}")

