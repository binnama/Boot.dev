def meditate(mana, max_mana, energy, energy_potions):

    while mana <= max_mana:
        if mana == max_mana:
            return mana, energy, energy_potions

        if energy == 0:
            if energy_potions > 0:
                energy += 50
                energy_potions -= 1
            else:
                return mana, energy, energy_potions


        while energy > 0:
            if mana == max_mana:
                return mana, energy, energy_potions
            elif mana == max_mana - 1:
                energy -= 1
                mana += 1
            elif mana == max_mana - 2:
                energy -= 1
                mana += 2
            else:
                energy -= 1
                mana += 3
        

    return mana, energy, energy_potions

