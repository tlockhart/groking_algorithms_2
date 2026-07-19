# What is the largets number in the List of numbers?

def find_max(numbers):
    # Base cases
    if len(numbers) == 1:
        return numbers[0]

    if len(numbers) == 0:
        return 0

    # Recursive case
    max_num = numbers.pop(0)      # Remove the first element
    next_num = find_max(numbers)

    if max_num > next_num:
        return max_num
    else:
        return next_num


numbers = [1, 2, 3, 4]
print("max_num:", find_max(numbers))
