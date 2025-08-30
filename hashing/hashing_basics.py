# Create an empty hash table (dictionary in Python)
hash_table = {}

# Insert key-value pairs into the hash table
hash_table['apple'] = 100
hash_table['banana'] = 200
hash_table['orange'] = 300

# Access values using keys
print('value of apple:', hash_table['apple'])
print('value of banana:', hash_table['banana'])

# Update a value
hash_table['apple'] = 150
print("Updated value of apple:", hash_table["apple"])

# Delete a key
del hash_table['banana']
print('hash table after deletion:', hash_table)
