#!/usr/bin/python3

from path import Path 

p = Path("testing.py")

# Check if the file exists
if p.exists():
    print(f"{p} exists!")

# Read file contents
if p.is_file():
    content = p.
    print("File content:", content)