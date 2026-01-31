import os

def read_file_lines(path):
    """Reads lines from a file and returns them as a list."""
    
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def write_file_lines(path, lines, append=True):
    """Writes a list of strings to a file."""
    
    mode = 'a' if append else 'w'
    with open(path, mode, encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def split_string(s, delimiter=','):
    """Splits a string based on a delimiter."""
   
    if s is None:
        return []
    return s.split(delimiter)

def input_int(prompt, low=None, high=None):
    """Safe integer input with range validation."""
    
    while True:
        try:
            value = int(input(prompt))
            if (low is not None and value < low) or (high is not None and value > high):
                print(f"Error: Value must be between {low} and {high}.")
                continue
            return value
        except ValueError:
            print("Error: Invalid integer. Please try again.")

def show_menu(choices):
    """Displays a menu list to the user."""
    
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}: {choice}")
    return input_int("Enter choice: ", 1, len(choices))