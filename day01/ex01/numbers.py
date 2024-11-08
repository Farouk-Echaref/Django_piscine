#!/usr/bin/python3

# forbidden (pass the filename directly)
import sys

def proccess_numbers_file(file_name: str) -> None:
    
    # open the file
    try:
        # with automatically closes the file when the with block ends
        with open(file_name, "r") as file:
            file_content = file.read()
            file_arr = file_content.split(",")
            for num in file_arr:
                print(num)
    except FileNotFoundError:
        print(f"Error: file '{file_name}' was not found.")
    except PermissionError:
        print(f"Error: you do not have persmission to read '{file_name}'.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    # else:
    #     print("File opened successfully.")
    
    # close the file
    try:
        file.close()
    except Exception as e:
        print(f"An unexpected error occured trying to close the file {file_name}: {e}")

if __name__ == "__main__":
    file_name = sys.argv[1]
    proccess_numbers_file(file_name)
    