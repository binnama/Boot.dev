def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        result = i % 2
        if result != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers
