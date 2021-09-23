# Python program to demonstrate sys.argv

from sys import argv
first, second, third = argv

print("The name of the program is: ", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

fourth = input("Guess what's next? ")

