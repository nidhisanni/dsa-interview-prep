class hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
        
    def hash_function(self, key):   # ✅ fixed: added self
        # Convert key (string) into a number using ASCII values
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)   # ✅ now works
        self.table[index].append((key, value))   # store key-value pair
    
    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)
            

# Create hash table of size 10
ht = hashtable(10)

# Insert key-value pairs
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("orange", 300)

# Retrieve values
print("Value of apple:", ht.get("apple"))
print("Value of banana:", ht.get("banana"))

# Display hash table
ht.display()
