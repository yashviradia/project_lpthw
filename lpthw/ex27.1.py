cars = input("cars: ")
people = input("people: ")
money = input("money: ")

if cars > people:
    if cars > money:
        print("Cars are too be sold at high price.")
    else:
        print("Some People will have to come on foot. Which is good for health.")
else:
    if people > money:
        print("We're out of money. Provide value to the market.")
    else:
        print("We're rich. Let's build a space colony on mars!")
