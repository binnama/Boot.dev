def find_max(nums):
    max_so_far = float("-inf")

    for value in nums:
        if value > max_so_far:
            max_so_far = value


    return max_so_far

