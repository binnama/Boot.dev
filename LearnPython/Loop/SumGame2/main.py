def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end):
        if(i % 2 != 0):
            total += i
    return total

# This is a solution from DC as I though modulo was not the expected way to 
# solve the task :)
def sum_of_odd_numbersSolution(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total
