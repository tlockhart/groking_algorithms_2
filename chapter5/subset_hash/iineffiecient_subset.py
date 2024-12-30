"""
By placing each number in the hash table as a key,
we can later look up each of those keys in one step.
If our lookup returns any value, it means the Key
itself must be in the hash table
"""
# O(n * m)
def is_subset(array1, array2):
    
    # Determine which array is smaller:
    if len(array1) > len(array2):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1
        
    # Iterate though smaller array:
    for i in smaller_array:
        
        # Found_match tracks whether the current element(i)
        # in the smaller array is present in the larger array.
        # It must be reset to false, each time an item in the
        # smaller array is checked
        
        found_match = False
        
        # For each value in smaller array, iterate through 
        # larger array:
        for j in larger_array:
            # if the two values are equal, it means the current
            # value in smaller array is present in the larger array:
            if i == j:
                found_match = True
                break;
        # If the current value in smaller array doesn't exist
        # in larger array, return false:
        if not found_match:
            return False
    
    # If we get to the end of the loops, it means that all 
    # values from smaller array are present in larger array:
    return True

array1 = ["a", "b", "c", "d", "e", "f"]
# array2 = ["b", "d", "f", "h"]
array2 = ["b", "d", "f"]

print(is_subset(array1, array2))
        