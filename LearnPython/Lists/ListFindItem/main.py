def contains_leather_scraps(items):
    found = False

    # don't touch above this line
    target = "Leather Scraps"

    for item in items:
        if item == target:
            found = True

    # don't touch below this line

    return found
