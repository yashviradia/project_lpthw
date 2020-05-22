from sys import argv

script, first, second = argv
prompt = '* '

print(f"Hi {first}, {second}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {first} and {second}?")
likes = input(prompt)

print(f"Where do you live {first} and {second}?")
lives = input(prompt)

print("In which country is that located?")
country = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}, which is in {country}. Not sure where that is.
And you have a {computer}. Nice.
""")
