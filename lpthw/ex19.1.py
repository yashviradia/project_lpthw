def wagen_und_zug(no_of_wagen, no_of_zug):
    print(f"Wir haben {no_of_wagen} wagen.")
    print(f"Wir haben auch {no_of_zug} zug.")
    print("Was soll ich jetzt machen?")
    print("Na ja, los geht's.\n")

print("Ich bin der Ansicht, dass es folgende Wagen gibt:")
wagen_und_zug(70, 40)

print("Wie viele wagen und zug hast du?")
wagen = input("wagen ?: ")
zug = input("züge ?: ")
wagen_und_zug(wagen, zug)

print("Was kann für Sie tun?")
umtauschen_wagen = input("Wie viele wagen möchten Sie umtauschen?: ")
umtauschen_züge = input("Wie viele züge möchten Sie umtauschen?: ")
wagen_und_zug(umtauschen_wagen, umtauschen_züge)


print("Ich kann sagen, dass ich soviele Wagen und Züge habe, aber nicht so viel wie Deutschland.")
meine_wagen = 1500
meine_züge = 4000
wagen_und_zug(meine_wagen, meine_züge)

print("Wie viele Wagen und Züge Deutschland eigentlich hat?")
wagen_und_zug(meine_wagen * 1020202, meine_züge * 203148)
