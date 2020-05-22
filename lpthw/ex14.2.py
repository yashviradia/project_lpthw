from sys import argv

script, eins, zwei, drei = argv
prompt = 'antwort: '

print(f"Hallo {eins}, {zwei} und {drei}, ich bin {script} script.")
print("Ich habe einige Fragen.")
print(f"Wie geht's {eins}, {zwei} und {drei}?")
greet = input(prompt)
print(f"Wie gefällt Sie hier?")
gefallen = input(prompt)

print(f"Wo wohnen {eins}, {zwei} und {drei}?")
wohnen = input(prompt)

print(f"Welcher Computer haben Sie?")
computer = input(prompt)

print(f"""
Also, es geht Ihnen {greet} und es gefällt Ihnen {gefallen}.
Sie wohnen in {wohnen}. Das weiß ich nicht.
Sie haben {computer} Computer. Das ist wunderbar.
""")
