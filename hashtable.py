class Hashtable:
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    def hash_func(self, key):
        return key % len(self.map)

    def size(self):
        num = 0
        for x in range(10):
            bucket_list = self.map[x]
            for item in bucket_list:
                num = num + 1
        return num

    # Inserts a new item into the hash table.

    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = self.hash_func(key)
        self.map[bucket].append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.

    def search(self, key):
        # get the bucket list where this key would be.
        bucket = self.hash_func(key)
        bucket_list = self.map[bucket]
        # print(bucket_list)

        # search for the item in the bucket list
        for item in bucket_list:
            if item.id == key:
                i = bucket_list.index(item)
                return bucket_list[i]
        else:
            return None

    # Removes an item with matching key from the hash table.

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = self.hash_func(key)
        bucket_list = self.map[bucket]

        # remove the item from the bucket list if it is present.
        for item in bucket_list:
            # print (key_value)
            if item.id == key:
                bucket_list.remove(item)