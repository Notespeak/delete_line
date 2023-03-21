import sys

def delete_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for index, line in enumerate(lines):
            if index != line_number - 1:
                file.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: delete_line.py <file_path> <line_number>")
        sys.exit(1)

    file_path = sys.argv[1]
    line_number = int(sys.argv[2])
    delete_line(file_path, line_number)
