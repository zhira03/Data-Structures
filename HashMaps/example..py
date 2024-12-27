from hashmaps import HashMap

# Instantiate the HashMap as a database
user_database = HashMap()

# Add users to the database
user_database['user1'] = {'name': 'Alice', 'email': 'alice@example.com'}
user_database['user2'] = {'name': 'Bob', 'email': 'bob@example.com'}
user_database['user3'] = {'name': 'Charlie', 'email': 'charlie@example.com'}

# Retrieve a user's details
print("Details of user1:")
print(user_database['user1'])

# Update a user's details
user_database['user2']['email'] = 'bob.new@example.com'
print("\nUpdated details of user2:")
print(user_database['user2'])

# Check if a user exists
print("\nDoes user3 exist?")
print('user3' in user_database)

# Delete a user
print("\nDeleting user1...")
del user_database['user1']
print(f"Is user1 still in the database? {'user1' in user_database}")

# Check if the database is empty
print("\nIs the database empty?")
print(user_database.is_empty())

# Print all users in the database
print("\nCurrent state of the database:")
print(user_database)

# Iterate over all user IDs
print("\nIterating over user IDs:")
for user_id in user_database:
    print(user_id)
