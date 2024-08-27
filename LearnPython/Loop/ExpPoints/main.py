def calculate_experience_points(level):
    total_exp = 0
    for i in range(1, level):
        exp_needed = i * 5
        total_exp += exp_needed

    return total_exp
