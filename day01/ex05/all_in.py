#!/usr/bin/python3

import sys

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        sys.exit()
    list_expr = sys.argv[1].split(",")
    print(list_expr)
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    pass