def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0
    for i in range(1, num_attacks + 1):
        if(i == num_attacks):
            damage = base_damage * 4
            total_damage += damage
        else:
            damage = base_damage * 2
            total_damage += damage

        #print(f"Attack {i}, current total damage: {total_damage}")

    return total_damage


