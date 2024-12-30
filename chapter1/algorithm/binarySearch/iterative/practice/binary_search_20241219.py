# I cracked my gold nugget
def low_not_over_high(low, high):
    return low <= high

def binary_search(items, item):
    # Init
    low = 0
    high = len(items) -1
    
    while low_not_over_high(low, high):
        # midpoint
        mid = (low + high) // 2
        guess = items[mid]
        # Conditions
        if guess == item:
            return mid
        # guess is over target, move high ptr backwards
        elif guess > item:
            high = mid - 1
        # guess is under target, move low ptr forward
        else:
            low = mid + 1
    # Not found
    return None


arr = [1,3,4,5,6]
print(binary_search(arr, 3))
print(binary_search(arr, 2))
