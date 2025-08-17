#unique voters registration system.

#voters name.

name = input("What is your name: ")

collection_of_voters = set()

collection_of_voters.add(name)

print(collection_of_voters)

another_name = input("What is your name: ")

collection_of_voters.add(another_name)

if another_name in name:
    print(f"WARNING:{another_name} YOU HAVE ALREADY VOTED!")
else:
    print("Thank you for exercising your constitutional right!")

print(len(collection_of_voters))