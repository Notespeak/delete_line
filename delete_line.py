#!/usr/bin/env python

import sys

def delete_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Could not read file '{file_path}': {e}")
        sys.exit(1)

    if line_number < 1 or line_number > len(lines):
        print(f"Error: Invalid line number {line_number}.")
        sys.exit(1)

    with open(file_path, 'w') as file:
        try:
            for index, line in enumerate(lines):
                if index != line_number - 1:
                    file.write(line)
        except IOError as e:
            print(f"Error: Could not write to file '{file_path}': {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: delete_line.py <file_path> <line_number>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        line_number = int(sys.argv[2])
    except ValueError:
        print("Error: Line number must be an integer.")
        sys.exit(1)

    delete_line(file_path, line_number)
