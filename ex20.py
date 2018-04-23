from sys import argv
#  Get's the input from terminal
script, input_file = argv

def print_all(t):
    # reads the file, f is only a reference
    print(t.read())

# function with a parameter
def rewind(v):
    # points a a position in the file, 
    # if '0' it's the beginning
    # '1' is the current position
    v.seek(0)

# function with two parameters
def print_a_line(line_count, t):
    # prints the number of the line, its content
    print(line_count, t.readline())

current_file = open(input_file)

print("Now let's rewind, kind of like a tape.")

print_all(current_file)

rewind(current_file)

print("let's print three lines: ")

current_line = 1
print_a_line(current_line, current_file)

print_a_line(current_line + 1, current_file)

print_a_line(current_line + 2, current_file)