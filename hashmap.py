import csv


class HashMap:
    def __init__(self):
        self.size = 50
        self.map = [None] * self.size

    def hashing_func(self, key):
        hashed_key = int(key) % self.size
        return hashed_key % self.size

    def add(self, key, address, city, state, zipcode, duetime, weight, special):
        hash_key = self.hashing_func(key)
        key_values = [key, address, city, state, zipcode, duetime, weight, special]

        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_values])
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = address
                    pair[2] = city
                    pair[3] = state
                    pair[4] = zipcode
                    pair[5] = duetime
                    pair[6] = weight
                    pair[7] = special
                    return True
            self.map[hash_key].append(key_values)
            return True

    def get(self, key):
        hash_key = self.hashing_func(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        hash_key = self.hashing_func(key)
        if self.map[hash_key] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()

with open('packages.csv', 'r') as file:
    readCSV = csv.reader(file, delimiter=',')
    for row in readCSV:
        h.add(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

h.print()
