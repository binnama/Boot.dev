def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line

    unpurchased_items = []
    receipt = {}
    total = 0

    for item in pinned_list:
        if item not in items_purchased:
            unpurchased_items.append(item)
            #print(f"Not in list: {unpurchased_items}")

    # This one is some loopy-SO-solution o.O See GPT for explanation!
    # We are creating a new dictionary `n` by iterating over each item `k` in the list `lis`.
    # For each item `k`, we check if `k` exists as a key in the dictionary `d`.
    # If the condition `k in d` is True, we add the key-value pair `k: d[k]` to the new dictionary `n`.

    # Breakdown:
    # - `for k in lis`: Loops over each element in the list `lis`. 
    #     Example: If `lis = ["item1", "item2", "item3"]`, `k` will first be `"item1"`, then `"item2"`, and so on.
    # - `if k in d`: Checks if the current item `k` is a key in the dictionary `d`.
    #     Example: If `k = "item1"` and `d = {"item1": "value1", "item3": "value3", "item4": "value4"}`, 
    #     the condition is True because `"item1"` exists as a key in `d`.
    # - `{k: d[k]}`: If `k` exists in `d`, it adds the key `k` and its corresponding value `d[k]` to the new dictionary `n`.
    #     Example: If `k = "item1"`, it adds `"item1": "value1"` to the new dictionary.

    # Result: `n` will contain only the key-value pairs from `d` where the key also exists in the list `lis`.

    receipt = {key: item_prices[key] for key in items_purchased if key in item_prices}
    #print(f"Receipt: {receipt}")

    total = receipt.values()
    total = sum(total)


    return unpurchased_items, receipt, total


