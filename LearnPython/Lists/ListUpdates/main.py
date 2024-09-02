def smelt_ore(inventory):

    target = "Iron Ore"

    for item in inventory:
        if item == target:
            inventory[1] = "Iron Bar"

    return inventory
