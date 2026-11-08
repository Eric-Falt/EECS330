class ChainingHashTable:
    """
    Hash Table using Open Hashing (Separate Chaining).
    Each slot stores a chain (Python list) of (key, value) pairs.
    """

    def __init__(self, size):
        """
        Initialize the hash table.
        param size: Table size (m)
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key: int) -> int:
        """Hash function: h(k) = k % m"""
        return key % self.size

    def insert(self, key: int, value: int):
        """
        Insert key-value pair using Chaining.
        On collision, append the pair to the end of the chain at that slot.
        """
        if not isinstance(key, int) or not isinstance(value, int):
            print("Error: Only integer keys and values are allowed.")
            return

        # Step 1: Compute the hash value
        # Step 2: Access the chain at that slot
        # Step 3: If the key already exists in the chain, update its value
        # Step 4: Otherwise, append (key, value) to the end of the chain
        chain = self.table[self._hash(key)]
        for index, (stored_key, _) in enumerate(chain):
            if stored_key == key:
                chain[index] = (key, value)
                return
        chain.append((key, value))

    def search(self, key: int):
        """Return the value stored for key, or None if the key is not found."""
        # Step 1: Compute the hash value
        # Step 2: Traverse the chain at that slot and compare each key
        # Step 3: If the chain ends without a match, the key is not in the table
        chain = self.table[self._hash(key)]
        for stored_key, stored_value in chain:
            if stored_key == key:
                return stored_value
        return None

    def display(self):
        """Display the hash table."""
        print("\n--- Final Hash Table (Chaining) ---")
        for i, chain in enumerate(self.table):
            if chain:
                print(f"Slot[{i}] → " + " → ".join(str(pair) for pair in chain))
            else:
                print(f"Slot[{i}] → None")


print("--- Question 1: Chaining ---")
hash_map = ChainingHashTable(size=7)
for k in [10, 17, 24, 31, 38, 45, 52, 59, 66]:
    hash_map.insert(k, k * 10)
hash_map.display()

for key in [24, 45, 70]:
    result = hash_map.search(key)
    if result is not None:
        print(f"Result: Key={key} → Value={result}")
    else:
        print(f"Result: Key={key} not found.")


## Expected Output:
# --- Question 1: Chaining ---
# --- Final Hash Table (Chaining) ---
# Slot[0] → None
# Slot[1] → None
# Slot[2] → None
# Slot[3] → (10, 100) → (17, 170) → (24, 240) → (31, 310) → (38, 380) → (45, 450) → (52, 520) → (59, 590) → (66, 660)
# Slot[4] → None
# Slot[5] → None
# Slot[6] → None
# Result: Key=24 → Value=240
# Result: Key=45 → Value=450
# Result: Key=70 not found.
