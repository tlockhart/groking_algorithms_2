"""
Uses open addressing with linear probing for collision handling. 
This means that when a collision occurs (i.e., two keys map to the same index), 
the table looks for the next available slot by incrementing the index until an 
empty slot is found.
"""
# Hungry raccoons ignore giant donuts.”

class HashTable:
    def __init__(self, initial_size=8):
        self.size = initial_size  # Table size
        self.count = 0            # Item count
        self.table = [None] * self.size  # The table (list)

    def _hash(self, key):
        """Simple hash function using modulus and a prime multiplier"""
        hash_value = 0
        # Step 1: Hash the key
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def _resize(self):
        """Resizes table when load factor exceeds 0.7"""
        new_size = self.size * 2  # Double the size
        new_table = [None] * new_size

        for item in self.table:
            if item:
                key, value = item
                new_index = self._hash_with_size(key, new_size)
                new_table[new_index] = (key, value)

        self.size = new_size
        self.table = new_table

    def _hash_with_size(self, key, size):
        """Hash function adjusted for custom table size"""
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % size
        return hash_value

    def insert(self, key, value):
        """Insert key-value pair into hash table"""
        # Step 2: resize when the load factor exceeds 0.7
        if self.count / self.size > 0.7:
            self._resize()  # Trigger resize if load factor is too high

        index = self._hash(key)
        # Step 3: Insert key value pair ( with collision handling)
        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index] = (key, value)  # Update existing key
                return
            index = (index + 1) % self.size  # Linear probing for collision

        self.table[index] = (key, value)  # Insert new key-value
        self.count += 1

    def get(self, key):
        """Retrieve value by key"""
        # Step 4: Get value by key
        index = self._hash(key)
        while self.table[index]:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        """Delete key-value pair by key"""
        # Step 5: Delete the key value pair
        index = self._hash(key)
        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                return
            index = (index + 1) % self.size

        raise KeyError("Key not found")

    def __repr__(self):
        """String representation of hash table"""
        return str([item for item in self.table if item])


# Example Usage
hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
hash_table.insert("city", "New York")

# Retrieving values
print(hash_table.get("name"))  # Output: Alice
print(hash_table.get("age"))   # Output: 30

# Inserting more items to trigger resizing
hash_table.insert("country", "USA")
hash_table.insert("job", "Engineer")
hash_table.insert("hobby", "Painting")
hash_table.insert("language", "English")
hash_table.insert("sports", "Tennis")  # Resizing triggered

# Check hash table content after resizing
print(hash_table)