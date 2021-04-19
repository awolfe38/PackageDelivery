# Functions to change the color of the output text
# O(1)
def print_red(skk):
    print("\033[91m {}\033[00m".format(skk))


def print_green(skk):
    print("\033[92m {}\033[00m".format(skk))


def print_yellow(skk):
    print("\033[93m {}\033[00m".format(skk))


def print_purple(skk):
    print("\033[95m {}\033[00m".format(skk))


def print_cyan(skk):
    print("\033[96m {}\033[00m".format(skk))


# Changes the number of minutes to a time format
# O(n)
def to_time(minutes):
    hours = minutes / 60
    mins = minutes % 60
    time = "%02d:%02d" % (hours, mins)
    return time


# Removes duplicate elements in a list and adds the hub
# O(n)
def alter(numbers):
    res = []
    for i in numbers:
        if i not in res:
            res.append(i)
    res.append(1)
    return res
