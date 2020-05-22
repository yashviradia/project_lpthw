# The total number of cars present
cars = 100
# Platz für jeder Person in dem Wagen
space_in_a_car = 4
# Gesamtnummer des Fahrers
drivers = 30
# Passegiere oder Fahrer
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
# car_pool_capacity isn't variable in the whole code
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
