# imports argument variable: sys is package and argv is feature
from sys import argv

# ask for argument to print
script, filename = argv

# Makes file object
txt = open(filename)

# usually prints the filename, f-string
print(f"Here's your file {filename}:")
# command to python '.' as read the file
print(txt.read())
print(txt.close())

# simple print
print("Type the filename again:")
# input with prompt
file_again = input("> ")

# command open
txt_again = open(file_again)

# command to python '.' to read the file
print(txt_again.read())
print(txt_again.close())
