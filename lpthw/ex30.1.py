people = input("people: ")
cars = input("cars: ")
trucks = input("trucks: ")

if cars > people and cars > trucks:
    print("We should take only exotic cars.")
elif people > cars and people > trucks:
    print("Manche Leute müssen zum Fuß gehen.")
else:
    print("What?!! Unfassbar!!!")

if cars > people or trucks > cars:
    print("This is insane.")
else:
    print("Das nimmt Schweiß aus mir.")
