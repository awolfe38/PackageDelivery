# Alexander Wolfe, student ID #001282336
import csv
from hashtable import *
from package import *
from utils import *

# Start the hash table
h = Hashtable()
# Read from the CSV file and add to the hash table
# O(n)
with open('packages.csv', 'r') as file:
    readcsv = csv.reader(file, delimiter=',')
    for row in readcsv:
        pack = Package(row)
        h.insert(pack.id, pack)

# Start the matrix graph
matrix = []
# Read from the CSV file and add to the matrix
# O(n)
with open('distances.csv', 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    for row in csvreader:
        matrix.append(row)


# Pathing Start
class Vertex:
    # Constructor for a new Vertx object.
    def __init__(self, label):
        self.label = label
        self.distance = 20.0
        self.pred_vertex = None


# Building the Graph
class Graph:
    # Constructor for the Graph object
    def __init__(self):
        self.adjacency_list = {}  # vertex dictionary {key:value}
        self.edge_weights = {}  # edge dictionary {key:value}
        self.total_distance = 0.0  # keeping track of how far each truck traveled
        self.vertex_list = []  # The locations each truck has to go
        self.start_time = 0  # The time each truck will leave the hub
        self.addresses = []  # List to hold all the addresses that need to be visited
        self.truck = []  # List to hold all the packages in each truck
        self.duo = {}  # dictionary that matches the package ID to the location

    # Add Vertex function
    # O(1)
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []  # {vertex_1: [], vertex_2: [], ...}
        self.vertex_list.append(new_vertex)

    # Adds a directed edge with the given weight in miles
    # O(1)
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        # {(vertex_1,vertex_2): 484, (vertex_1,vertex_3): 626, ...}
        self.adjacency_list[from_vertex].append(to_vertex)
        # {vertex_1: [vertex_2, vertex_3], vertex_2: [vertex_6], ...}

    # Adds undirected edges by calling the add_directed_edge function twice while switching the vertices
    # O(1)
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


# Initiates three graphs, one for each truck and path
# O(1)
a = Graph()
b = Graph()
c = Graph()

# Manually sort packages into three trucks
# O(1)
a.truck = [13, 26, 34, 29, 30, 14, 15, 16, 19, 20, 1, 37, 40, 21, 4]
b.truck = [3, 18, 36, 28, 31, 32, 2, 38, 6, 25]
c.truck = [24, 27, 33, 35, 10, 11, 12, 17, 22, 23, 39, 5, 7, 8, 9]

# Give the trucks their start times
# O(1)
a.start_time = 480
b.start_time = 550
c.start_time = 620

# Initiates three lists to hold the addresses that need to be visited by each truck
# O(n^2)
for i in range(0, len(a.truck)):
    package = h.search(a.truck[i])
    for j in range(0, len(matrix)):
        if matrix[j][1].__contains__(package.address):
            a.addresses.append(j + 1)
            a.duo[a.truck[i]] = j + 1

for i in range(0, len(b.truck)):
    package = h.search(b.truck[i])
    for j in range(0, len(matrix)):
        if matrix[j][1].__contains__(package.address):
            b.addresses.append(j + 1)
            b.duo[b.truck[i]] = j + 1

for i in range(0, len(c.truck)):
    package = h.search(c.truck[i])
    for j in range(0, len(matrix)):
        if matrix[j][1].__contains__(package.address):
            c.addresses.append(j + 1)
            c.duo[c.truck[i]] = j + 1

# O(n)
a.addresses = alter(a.addresses)
b.addresses = alter(b.addresses)
c.addresses = alter(c.addresses)

# Goes through the addresses and adds the appropriate vertex
# O(n)
for i in a.addresses:
    a.add_vertex(i)
for i in b.addresses:
    b.add_vertex(i)
for i in c.addresses:
    c.add_vertex(i)

# Adds all the edges between each vertex with the appropriate weight in miles
# O(n^2)
for i in a.addresses:
    for j in a.addresses:
        if j > i:
            a.add_undirected_edge(j, i, float(matrix[j - 1][i + 1]))

for i in b.addresses:
    for j in b.addresses:
        if j > i:
            b.add_undirected_edge(j, i, float(matrix[j - 1][i + 1]))

for i in c.addresses:
    for j in c.addresses:
        if j > i:
            c.add_undirected_edge(j, i, float(matrix[j - 1][i + 1]))


# Finds the closest location that still needs packages delivered to
# O(n)
def nearest_neighbor(g, current, available):
    dist = 30.0
    near = 0
    for vertex in g.edge_weights:
        (first, second) = vertex
        while first == current and available.__contains__(second) and g.edge_weights[vertex] < dist:
            dist = g.edge_weights[vertex]
            near = second
    g.total_distance += dist
    # Returns the next nearest vertex and the distance needed to travel
    return near, dist


# Uses the above function to find the path that constantly finds the next shortest vertex
# O(n^2)
def run_path(g, start, time):
    # Correct Address on package #9
    if time >= 620:
        h.search(9).address = "410 S State St."
        h.search(9).zipcode = "84111"
        b.duo.update({9: 20})
        if g.edge_weights == c.edge_weights:
            if g.vertex_list.__contains__(13):
                g.vertex_list.remove(13)
    # Update status of package when leaving the hub
    if g.start_time < time:
        for i in g.truck:
            h.search(i).status = "En Route"
    # Keeps track of which vertices we still have yet to visit
    unvisited = g.vertex_list
    while len(unvisited) > 0:
        if unvisited.__contains__(1):
            unvisited.remove(1)

        # Uses the nearest_neighbor function and returns the nearest location and the distance needed to travel
        x, y = nearest_neighbor(g, start, unvisited)
        # Adds the time need to travel to the next location to see if there is enough time to make it there
        g.start_time += (y * 60 / 18)
        # Ends the loop if the given time is earlier than the time the truck will arrive at the next location
        if g.start_time > time:
            break
        # Update the status and delivery time of the newly delivered packages
        for p_id, loc in g.duo.items():
            if loc == x:
                h.search(p_id).status = "Delivered!"
                h.search(p_id).time = to_time(g.start_time)
        # Removes the vertex from the unvisited list
        unvisited.remove(x)
        # Replaces the previous vertex with the vertex we just arrived at
        start = x

    # Send truck 1 back to hub so the driver can move to truck 3
    if g.edge_weights == a.edge_weights and g.start_time < time:
        nearest_neighbor(g, start, [1])


# Starts the main menu prompt
home1 = "WELCOME TO THE PACKAGE DELIVERY PROGRAM"
home2 = "1|Find the total distance traveled by each truck\n 2|Find the delivery status of each package at a certain " \
        "time\n 3|Look up a specific package\n 4|Exit "

print_purple(home1)
print_cyan(home2)
option = ""
while option != "4":
    option = input("Please select one of the options(Type 1-4):")
    # Returns the total distances
    # O(1)
    if option == "1":
        run_path(a, 1, 1200)
        run_path(b, 1, 1200)
        run_path(c, 1, 1200)
        print_yellow("Truck 1 traveled: %.1f" % round(a.total_distance, 1))
        print_yellow("Truck 2 traveled: %.1f" % round(b.total_distance, 2))
        print_yellow("Truck 3 traveled: %.1f" % round(c.total_distance, 2))
        print_red("Total distance traveled: %.1f" % round((a.total_distance + b.total_distance + c.total_distance),
                                                          2) + "\n\n\n")
        print_cyan(home2)
    # Returns the status of all the packages at a certain time
    # O(n)
    elif option == "2":
        option2 = ""
        print_green("\nWhat time do you wish to see the status of the packages?")
        while option2 != "0":
            option2 = input("Type the time with the number of minutes i.e. 3pm = 900 or enter 0 to go back:")
            run_path(a, 1, int(option2))
            run_path(b, 1, int(option2))
            run_path(c, 1, int(option2))
            for x in range(1, 41):
                h.search(x).print_package()
            h.search(9).address = "300 State St"
            h.search(9).zipcode = "84103"
            print("\n\n\n")
        print_cyan(home2)

    elif option == "3":
        # Returns the status of a single package
        # O(1)
        option2 = ""
        print_green("\nWhat package do you want to find the status of?")
        while option2 != "0":
            option2 = input("Type the package ID (Type 0 to go back):")
            run_path(a, 1, 1200)
            run_path(b, 1, 1200)
            run_path(c, 1, 1200)
            if 0 < int(option2) < 41:
                h.search(int(option2)).print_package()
            else:
                print_purple("Package not found")
            print("\n\n\n")
        print_cyan(home2)
