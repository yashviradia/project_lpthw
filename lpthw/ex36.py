# das Spiel in dem Raum

from sys import exit

def mineral_zimmer():
    print("Dieses Zimmer hat viel Mineral. Wie viel nimmst du?")

    wahl = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Mensch, lern die Nummer einzugeben!")

    if how_much < 50:
        print("Gut, Du bist nicht gierig, du hast gewonnen!")
        exit(0)
    else:
        dead("Du bist geriger Bastard!")

def ausserirdische_raum():
    print("Dort ist ein ausserirdischer.")
    print("Er hat viel Mineral.")
    print("ausserirdischer, der vor der Tür steht, ist sehr dick.")
    print("Wie wirst du den bewegen?")
    ausserirdischer_bewegt = False

    while True:

        wahl = input("> ")

        if wahl == "nimm Mineral":
            dead("der ausserirdische hat angst von dir, er geht weg")
        elif wahl == "Schrei" and not ausserirdischer_bewegt:
            print("der ausserirdische ist weggegangen.")
            print("du kannst jetzt reingehen.")
            ausserirdischer_bewegt = True
        elif wahl == "Schrei" and ausserirdischer_bewegt:
            dead("der ausserirdische schreit sehr laut und ist gestorben.")
        elif wahl == "mach die Tür aus" and ausserirdischer_bewegt:
            mineral_zimmer()
        else:
            print("Ich habe eine Idee, was das bedeutet.")

def sitzung_raum():
    print("Hier siehst du SpaceX Firma.")
    print("Dort ist Musks Büro.")
    print("Was willst du machen?")

    wahl = input("> ")

    if "treffen" in wahl:
        print("Du triffst mit Elon Musk und redest über die neuen Ideen.")
        print("Er ist von deiner Ideen sehr überrascht und will dir etwas schenken.")
        print("Hier gibt es verschiedene Schenken. Was willst du nehmen?")

        zettel = ['Model S', 'Model X', 'Model 3', 'Model Y', 'Dragon capsule', 'Falcon 5']
        print(zettel)

        wahl = input("> ")

        if wahl == "nicht":
            print("Er will dir Model S, Model X, Model Y, Dragon capsule, Falcon 5 schenken.")
        else:
            print("Du bist nicht so gierig!")
    elif "Handschlag" in wahl:
        print("Du kannst nur 5 Minuten sitzen.")
    else:
        sitzung_raum()

def dead(warum):
    print(warum, "Gut gemacht!")
    exit(0)

def start():
    print("Du bist in einem dunklen Raum.")
    print("Links und rechts sind die Tür.")
    print("Welche nimmst du?")

    wahl = input("> ")

    if wahl == "links":
        ausserirdische_raum()
    elif wahl == "rechts":
        sitzung_raum()
    else:
        dead("Mensch, du musst Deutsch sehr viel lernen.")


start()
