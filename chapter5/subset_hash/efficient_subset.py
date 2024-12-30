# O(n + m) = O(n)
# mneumonic: I-Always Cut-Large-Hashbrowns Carefully
def is_subset(array1, array2):
     # Identify (Arrays) small and large array:
    if len(array1) > len(array2):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1
    
    # Create a hash table in python
    hash_table = {}
    
    # (Cut large hashbrowns) Convert larger_array to hash_table
    for value in larger_array:
        hash_table[value] = True
    # (Carefully) Check if smaller_array value is subset of hash_table
    for value in smaller_array:
        if not hash_table.get(value):
            return False
    # If code gets this far then all smaller elements in larger element
    return True

array1 = ["a", "b", "c", "d", "e", "f"]
array2 = ["b", "d", "f", "h"]
# array2 = ["b", "d", "f"]

print(is_subset(array1, array2))