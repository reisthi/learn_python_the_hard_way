# this tells the system we are importing a module
from sys import argv

# this assigns the value of argv into two variables
script, filename = argv

# this opens a file named with the name we 
# grabbed form the user when he inputs the second argument
txt = open(filename)

print(f"Here;s yout file {filename}: ")
#this reads the file
# print(txt.write('Ulalalalulelelele'))
# print(txt.save())
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())