def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):

    if (player_name == high_scoring_player_name):
        result = "high"
    elif (player_name == low_scoring_player_name):
        result = "low"
    else:
        result = "neither"

    return result
