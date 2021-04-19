class Package(object):
    def __init__(self, pair):
        self.id = int(pair[0])
        self.address = pair[1]
        self.city = pair[2]
        self.state = pair[3]
        self.zipcode = int(pair[4])
        self.due = pair[5]
        self.weight = int(pair[6])
        self.message = pair[7]
        self.status = "At the hub"
        self.time = "N/A"

    # Prints the total information of the package
    def print_package(self):
        print("ID: %i|Address: %s|City: %s|State: %s|Zip Code: %s|Due By: %s|Weight: %s|Message: %s|Status: "
              "%s|Delivered At: %s "
              % (self.id, self.address, self.city, self.state, self.zipcode, self.due,
                 self.weight, self.message, self.status, self.time))
