# I Always Cut Large Hashbrowns Carefully
def is_subset(array1, array2):
    small_array = []
    large_array = []
    # Identify arrays (small, large)
    if len(array1) < len(array2):
        small_array = array1
        large_array = array2
    else:
        small_array = array2
        large_array = array1
    # Convert
    hash_table = {}
    item_found = False
    
    for value in large_array:
        hash_table[value] = True
        
    # Check subset
    for item in small_array:
        if hash_table.get(item):
            item_found = True
        else:
            item_found = False
            return item_found
    return True

# small = ['apple', 'paper', 'dog', 'cat']
small = ['apple', 'paper', 'dog', 'cat', 'shiny']
large = ['apple', 'orange', 'paper', 'dog', 'cat', 'possum']

print(is_subset(small, large))
        
        
    