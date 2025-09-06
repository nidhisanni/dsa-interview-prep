class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]  # list of lists

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # check if key already exists → update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # otherwise, add new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


# -------------------
# TESTING COLLISION
# -------------------
ht = HashTable()

# inserting keys
ht.insert("bat", 500)
ht.insert("tab", 600)   # will collide with "bat"
ht.insert("apple", 100)

# display the whole table
ht.display()

# retrieving both
print("bat:", ht.get("bat"))
print("tab:", ht.get("tab"))
print("apple:", ht.get("apple"))
 
 
 