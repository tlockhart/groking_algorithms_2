def low_not_over_high(low, high):
    return low <= high

# I cracked my gold nugget

def binary_search(items, target):
    # Initialize
    low = 0
    high = len(items) - 1
    
    # Check No Cross condition:
    while low_not_over_high(low, high):
        # set midpoint
        mid = (low + high) // 2
        guess = items[mid]
        # Goldilocks condition
        if guess == target:
            return mid;
        # If guess too high, the middle index is over 
        # the target, so move the window back 
        # by shifting high backwards
        elif guess > target:
            high = mid - 1
        # If guess too low, the middle index is 
        # under the target, so move the window 
        # foward by shifting low forward
        elif guess < target:
            low = mid + 1
    # If nothing found return None 
    return None

arr = [1,3,4,5,6]
print(binary_search(arr, 1))
print(binary_search(arr, 2))