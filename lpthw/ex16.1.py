from sys import argv

script, reading_file = argv

print(f"Here is your {script} script")
input("What do you want?: ")
print("Opening the file....")

target = open(reading_file)
print(target.read())
