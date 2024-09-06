def get_champion_slices(champions):

    champ_list_1 = []
    champ_list_2 = []
    champ_list_3 = []

    champ_list_1 = champions[2:]
    champ_list_2 = champions[:-2]
    champ_list_3 = champions[::2]

    return champ_list_1, champ_list_2, champ_list_3
