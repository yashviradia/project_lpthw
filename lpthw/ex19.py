# creates a function of cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# giving amount to the arguments in the function
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# giving values to the variables
amount_of_cheese = 10
amount_of_crackers = 50

# assigning variables into the function cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# addition in the function cheese_and_crackers
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# doing math with the variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers * 21)
