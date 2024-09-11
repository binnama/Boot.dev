def get_most_common_enemy(enemies_dict):

    max_so_far = float("-inf")
    common_enemy = ""

    if bool(enemies_dict) == False:
        return None


    for enemy in enemies_dict:
        size = enemies_dict[enemy]
        print(enemy)

        if size > max_so_far:
            max_so_far = size
            common_enemy = enemy


    return common_enemy




