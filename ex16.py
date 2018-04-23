#  This gets two arguments, the file and an input from terminal
from sys import argv
 
#  This assigns those two arguments to the variables script and filename
script, filename = argv

# This prints filename
print(f"We are going to erase {filename}.")
print('''
Type CTRL + C to cancel.
Or type RETURN to erase the file.''')

# gets the input from the user
input("?")

print("Opening the file...")
# This creates an object that opens the file
target = open(filename, 'w')

print("Truncating the file...")
# This erases the file
target.truncate()

print("Now we are going to ask you three lines")

#  This gets inputs from the user and assign them to variables
line1 = input("line one: ")
line2 = input("line two: ")
line3 = input("line three: ")

print(f"Adding them to {filename}...")

#  This writes the values of the variables to the file
target.write(line1 + '\n' + line2 + '\n' + line3)

print("Closing the file...")
#  Closes the file
target.close()