def low_not_over_high(low, high):
    return low <= high

# I cracked my gold nugget
# Removed the for loop, in order
# to use the stack to repeat the 
# calls, until the item is found.

# Note: Since high must be calculated 
# initially set it to None and add a 
# condition to set it for the first time
def binary_search(items, target, low=0, high=None):
    # Initialize
    if high == None:
        high = len(items) - 1
    mid = (low + high) // 2
    
    # Base, is if low crosses high
    if low > high or high < 0: return None
    
    guess = items[mid]
   
    # Goldilocks condition
    
    # if guess == target item found
    if items[mid] == target:
        return mid;
    # If guess too high, the middle index is over 
    # the target, so move the window back 
    # by shifting high backwards
    elif guess > target:
        high = mid - 1
        # print(high)
    # If guess too low, the middle index is 
    # under the target, so move the window 
    # foward by shifting low forward
    elif guess < target:
        low = mid + 1
    
    # Recursive Call:
    item_found = binary_search(items, target, low, high)
    # print("itemfound:", item_found)
    return item_found

arr = [1,3,4,5,6]
print(binary_search(arr, 1))
# print(binary_search(arr, 2))