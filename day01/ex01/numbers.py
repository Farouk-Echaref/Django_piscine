#!/usr/bin/python3

# forbidden (pass the filename directly)
import sys

def proccess_numbers_file(file_name: str) -> None:
    file = open(file_name, "r")
    print(file.readline())


if __name__ == "__main__":
    file_name = sys.argv[1]
    proccess_numbers_file(file_name)
    
    
    
    
    try:
    file = open(file_name, "r")
    # You can now work with the file, e.g., file.read()
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    # Optional: Actions to take if no exception occurred
    print("File opened successfully.")
finally:
    # Clean up by closing the file if it was opened successfully
    try:
        file.close()
    except NameError:
        pass
