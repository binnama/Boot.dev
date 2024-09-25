def merge(dict1, dict2):
    #print(f"Dict 1: {dict1}")
    #print(f"Dict 2: {dict2}")
    merged_dicts = dict1.copy()
    merged_dicts.update(dict2)

    #print(f"Merged Dicts: {merged_dicts}")
    return merged_dicts

def total_score(score_dict):
    sum_score = 0
    temp_score = score_dict.values()
    sum_score = sum(temp_score)

    return sum_score


