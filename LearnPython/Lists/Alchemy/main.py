def check_ingredient_match(recipe, ingredient):

    percentage = 0
    exists = 0
    required = len(recipe)
    ingredients = []

    # Placement matters!
    for i in range(len(recipe)):
        if recipe[i] == ingredient[i]:
            exists += 1
        else:
            ingredients.append(recipe[i])

    percentage = (exists / required) * 100

    return percentage, ingredients
