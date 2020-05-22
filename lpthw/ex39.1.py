# create a mapping of state of abbreviation
states = {
            'Schleswig-Holstein': 'SH',
            'Mecklenburg-Vorpommen': 'MV',
            'Bayern': 'BY',
            'Brandenburg': 'BB',
            'Sachsen': 'SN',
            'Niedersachsen': 'NI',
            'Sachsen-Anhalt': 'ST',
            'Hessen': 'HE',
            'Saarland': 'SL',
            'Berlin': 'BE',
            'Hamburg': 'HH',
            'Bremen': 'HB',
            'Nordrhein-Westfalen': 'NW',
            'Rheinland-Pfalz': 'RP',
            'Thüringen': 'TH',
            'Baden-Württemberg': 'BW'
}

# create a basic set of states and some cities in them
cities = {
    'BE': 'Berlin',
    'SH': 'Kiel',
    'TH': 'Weimar',
    'HH': 'Hamburg',
    'MV': 'Rostock',
    'HE': 'Frankfurt',
    'SN': 'Chemnitz',
    'BB': 'Postdam',
    'NI': 'Clausthal',
    'SL': 'Saarbrücken',
    'NW': 'Aachen',
    'HB': 'Bremen',
    'RP': 'Bonn',
    'ST': 'Magdeburg'
}

# add some more cities
cities['BW'] = 'Stuttgart'
cities['BY'] = 'München'

# print out some cities
print('-' * 10)
print("SH Bundesland hat: ", cities['SH'])
print("TH Bundesland hat: ", cities['TH'])

# print some states
print('-' * 10)
print("Hamburgs Abkürzung ist: ", states['Hamburg'])
print("Nordrhein-Westfalen ist: ", states['Nordrhein-Westfalen'])

# do it by using the state then cities dict
print('-' * 10)
print("Schleswig-Holstein hat: ", cities[states['Schleswig-Holstein']])
print("Thüringen hat: ", cities[states['Thüringen']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be There
state = states.get('Hamburg')

if not state:
    print("Sorry, that state doesn't exist.")
else:
    print("Ja, Hamburg liegt in NordDeutschland.")
