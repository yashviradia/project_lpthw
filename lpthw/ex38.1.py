print("""Here's the list of countries sharing the border
with the Germany including Germany.""")

land = ['Deutschland', 'Daenmark', 'Der Schweiz', 'Oesterrich',
        'Niederlaender', 'Belgium', 'Luxemburg', 'Polen',
        'Czech Republik']
print(land)
print(land[0:5:2])
print(land[0:7:3])
print(land[0:8:8])
print('This country is great and thriving '.join(land[0:8:8]))
