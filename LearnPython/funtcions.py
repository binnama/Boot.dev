# Funcitons 
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")

# Multiple parameters
print("")
def triple_attack(damage_one, damage_two, damage_three):
    total = damage_one + damage_two + damage_three
    return total

attack_one = 2
attack_two = 4
attack_three = 3
attack_four = -1
attack_five = 10
attack_six = 5

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(triple_attack(attack_one, attack_two, attack_three), "points of damage dealt!")
print("=====================================")

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(triple_attack(attack_four, attack_five, attack_six), "points of damage dealt!")
print("=====================================")

# Multiple return values
print("")
def become_warrior(first_name, last_name, power):
    title = (f"{first_name} {last_name} the warrior")  # format the person's title
    new_power = power  # replace with the correct value
    return title, new_power

# Don't edit below this line

def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)

def test(first_name, last_name, power):
    title, new_power = become_warrior(first_name, last_name, power)
    print(title, "has a power level of:", new_power)

main()
