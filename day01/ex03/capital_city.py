#!/usr/bin/python3

import sys

def process_dict(state_search: str, states: dict, capital: dict) -> str:
    state_brev = states.get(state_search, None)
    if state_brev == None:
        return "Unknown state"
    cap_name = capital_cities[state_brev]
    
    return cap_name

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        sys.exit()
    
    state_name = sys.argv[1]
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

    print(process_dict(state_name, states, capital_cities))