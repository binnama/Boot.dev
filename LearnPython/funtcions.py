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

# Default values for funticon arguments
print("")

def get_punched(health, armor = 0):
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor = 0):
    damage = 100 - armor
    new_health = health - damage
    return new_health


def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("=====================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("=====================================")

test(400, 5)
test(300, 3)
test(200, 1)

#Curse 
print("")

def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.75
    return lesser_cursed, greater_cursed

def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")

def main():
    test(100)
    test(500)
    test(1000)

main()

# Enchant and attack
print("")

def enchant_and_attack(target_health, damage, weapon):
    enchanted_damage = damage + 10
    new_health = target_health - enchanted_damage
    enchanted_weapon = "enchanted " + weapon
    return enchanted_weapon, new_health

def test(target_health, damage, weapon):
    print("The target has", target_health, "health.")
    print(weapon, "base damage:", damage, "Enchanting and attacking")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print("The target has been attacked with the", enchanted_weapon)
    print("The target has", new_health, "health remaining.")
    print("=====================================")

def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")

main()
