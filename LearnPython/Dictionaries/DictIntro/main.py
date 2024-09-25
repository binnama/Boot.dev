def get_character_record(name, server, level, rank):

    id = f"{name}#{server}"

    character_dict = dict(name = name, server = server, 
                          level = level, rank = rank,
                          id = id)

    return character_dict
