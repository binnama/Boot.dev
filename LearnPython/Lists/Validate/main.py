def validate_path(expected_path, character_path):
    
    character_name = character_path[0]
    percetage = 0
    required_path = len(expected_path)
    actual_path = 0
    index = 0

    for path in character_path[1:]:
        if path == expected_path[index]:
            actual_path += 1

        index += 1

    percetage = (actual_path / required_path) * 100

    return character_name, percetage


