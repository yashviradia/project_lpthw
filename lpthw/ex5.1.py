his_name = 'Yash R. Viradia'
his_age = 19 # not a lie
his_height = 74 # inches
his_weight = 180 # lbs
his_eyes = 'Blue'
his_teeth = 'White'
his_hair = 'Brown'

print(f"Let's talk about {his_name}.")
print(f"He's {his_height} inches tall.")
print(f"He's {his_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {his_eyes} eyes and {his_hair} hair.")
print(f"His teeth are usually {his_teeth} depending on the milk.")

# this line is tricky, try to get it exactly right
total = his_age + his_height + his_weight
print(f"If I add {his_age}, {his_height}, and {his_weight} I get", total)

# 1 inch = 2.54 centimeters
# 1 kg = 2.205 pounds

true_weight = 180 / 2.205 # kilograms
true_height = 74 * 2.54 # centimeters
print(true_weight)
print(true_height)
