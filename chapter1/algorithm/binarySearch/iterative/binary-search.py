def is_high_above_low(low, high):
    return low <= high

# Pneumoic: I cracked my gold nugget
# Init, Cross Check, Midpoint, Goldilocks Conditions, Not found)
def binary_search(arr, item):
    # Step 1: Initialize start and end index
    low = 0
    high = len(arr) - 1
    # Step 2: Check if high above low
    while is_high_above_low(low, high):
        # Step 3: Find the middle array index
        mid = (low + high) // 2
        # Step 4: Compare the guess using the 3 GoldiLock conditions
        guess = arr[mid]
        # Step 4A: Is guess just right (equal), return mid
        if guess == item:
            return mid
        # Step4B: Is guess too large, move high index before mid
        elif guess > item:
            high = mid -1
        # Step 4C: Is guess <= item, move low index after mid
        else:
            low = mid + 1
    # Return None if not found
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None