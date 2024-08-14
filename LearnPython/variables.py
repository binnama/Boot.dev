# Variables
player_health = 1000

print(player_health)

# Variables vary
print("")

player_health = player_health - 100
print(player_health)

player_health = player_health - 100
print(player_health)

player_health = player_health - 100
print(player_health)

player_health = player_health - 100
print(player_health)

# Let's do some math
print("")
player_health = 1000

armor_multiplier = 2
armored_health = player_health * armor_multiplier
print(armored_health)

# And some more math
print("")
player_health = 100
poison_damage = 10

player_poison_health = player_health - poison_damage
print(player_poison_health)

# Basic variable types
print("")

player_health = 100

player_has_magic = True

print(f"player_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")

# f-strings in python
print("")

name = "Yarl"
age = 37
race = "dwarf"

print(f"{name} is a {race} who is {age} years old.")

# Nonetype Variables
print("")
enemy = None
print(enemy is None)

# Math with strings
print("")
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)

# Battleground Average
print("")
game_one_score = 97
game_two_score = 91
game_three_score = 106
game_four_score = 105
game_five_score = 96
game_six_score = 93
game_seven_score = 104

average_score = (game_one_score + game_two_score + game_three_score + game_four_score + game_five_score + game_six_score + game_seven_score) / 7

print(round(average_score))
