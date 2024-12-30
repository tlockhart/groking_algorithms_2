import random
# O(n log n)
# Brave - Pirates Plunder - Diamond Stones - Loving - Gold - Rings - Constantly
def quickSort(items):
    # Base Case
    if len(items) <= 1:
        return items
    
    # Pop Pivot:
    index = random.randint(0, len(items) -1)
    pivot_element = items.pop(index)
    
    # Declare Subarrays:
    center_array = [pivot_element]
    smaller_array = []
    larger_array = []
    
    # Loop
    while len(items) > 0:
        current_element = items.pop()
        
        # Goldlock conditions:
        if current_element == pivot_element:
            center_array.append(current_element)
        elif current_element < pivot_element:
            smaller_array.append(current_element)
        elif current_element > pivot_element:
            larger_array.append(current_element)
    
    # recursive sort:
    smaller_sorted_array = quickSort(smaller_array)
    larger_sorted_array = quickSort(larger_array)
    
    # Concatenate
    return smaller_sorted_array + center_array + larger_sorted_array

items = [5, 1, -9, 3, 2, 1, 0]
print(quickSort(items))