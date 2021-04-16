import csv
from hashtable import *
from package import *
from utils import *

# Manually sort packages into 3 trucks
truck_A = [13, 14, 15, 16, 19, 1, 26, 34, 29, 30, 37, 40, 21, 4]
truck_B = [3, 6, 25, 28, 31, 32, 2, 7, 20, 18, 36, 38]
truck_C = [5, 8, 22, 23, 24, 27, 9, 10, 11, 12, 17, 33, 35, 39]

# Start the hash table
h = Hashtable()
# Read from the CSV file and add to the hash table
with open('packages.csv', 'r') as file:
    readcsv = csv.reader(file, delimiter=',')
    for row in readcsv:
        pack = Package(row)
        h.insert(pack.id, pack)

# Start the matrix graph
matrix = []
# Read from the CSV file and add to the matrix
with open('distances.csv', 'r') as file:
    readcsv = csv.reader(file, delimiter=',')
    for row in readcsv:
        matrix.append(row)

# Starts the main menu prompt
home1 = "WELCOME TO THE PACKAGE DELIVERY PROGRAM"
home2 = "1|Find the total distance traveled by each truck\n 2|Find the delivery status of each package at a certain " \
        "time\n 3|Look up a specific package\n 4|Exit "

print_purple(home1)
print_cyan(home2)
option = ""

while option != "4":
    option = input("Please select one of the options(Type 1-4):")

    if option == "1":
        print_red("Total distance traveled: 0\n\n\n")
        print_cyan(home2)

    elif option == "2":
        option2 = ""
        print_yellow("\nWhat time do you wish to see the status of the packages?")
        while option2 != "0":
            option2 = input("Type the time with the number of minutes i.e. 3pm = 900 or enter 0 to go back:")
            print_red("-----\n\n\n")
        print_cyan(home2)

    elif option == "3":
        option2 = ""
        print_green("\nWhat package do you want to find the status of?")
        while option2 != "0":
            option2 = input("Type the package ID (Type 0 to go back):")
            print_red("-----\n\n\n")
        print_cyan(home2)

