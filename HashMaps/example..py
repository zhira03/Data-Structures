from hashmaps import HashMap
import uuid

# Instantiate the HashMap as a database
def userDatabase():
    user_database = HashMap()

    # Add users to the database
    user1_id = str(uuid.uuid4())
    user2_id = str(uuid.uuid4())
    user3_id = str(uuid.uuid4())


    user_database[user1_id] = {'name': 'Alice', 'email': 'alice@example.com'}
    user_database[user2_id] = {'name': 'Bob', 'email': 'bob@example.com'}
    user_database[user3_id] = {'name': 'Charlie', 'email': 'charlie@example.com'}

    newName = input("What is your name? ")
    newEmail = input("What is your email address? ")

    user4_id = str(uuid.uuid4())
    user_database.__setitem__(user4_id, {'name': newName, 'email': newEmail})

    print(user_database.__str__())

    # Retrieve a user's details
    print("Details of user1:")
    print(user_database[user1_id])

    # Update a user's details
    user_database[user2_id]['email'] = 'bob.new@example.com'
    print("\nUpdated details of user2:")
    print(user_database[user2_id])

    # Check if a user exists
    print("\nDoes user3 exist?")
    print(user_database.contains(user3_id))

    # Delete a user
    print("\nDeleting user1...")
    user_database.__delitem__(user1_id)
    print(f"Is user1 still in the database? {user_database.contains(user1_id)}")    

    # Check if the database is empty
    print("\nIs the database empty?")
    print(user_database.is_empty())

    # Print all users in the database
    print("\nCurrent state of the database:")
    print(user_database.__str__())

    user_database.clear()
    print(user_database.contains(user3_id))

    print(user_database.__str__())


people = userDatabase()
print(people)
