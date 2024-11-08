#!/usr/bin/python3

import sys

def process_dict(capital_search: str, states: dict, capital: dict) -> str:
    state_brev = [name for name in capital if capital[name]==capital_search]
    if len(state_brev) == 0:
        return "Unknown capital city"
    state_name = [name for name in states if states[name]==state_brev[0]]
    
    return state_name[0]

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        sys.exit()
    
    capital_name = sys.argv[1]
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
    
    print(process_dict(capital_name, states, capital_cities))