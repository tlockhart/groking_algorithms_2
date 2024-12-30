import random

# Mnemonic: Bold Pirates Plunder Diamond Stones, Loving Gold Rings Constantly
def sort(numbers):
    # copied_array = numbers.copy()
    copied_array = numbers[0:]
    
    # Base Case:
    # if copied_array len is empty array or has 
    # 1 item, return it, nothing to partition
    if len(copied_array) <= 1:
        return copied_array
        

    # Pop Pivot element: Deprecated, will cause n^2 runtime if list sorted
    # pivot_element = copied_array.pop(0)
    
    # random.random() generates a random float between 0 and 1 (exclusive)
    # randint generates a random integer between the first and second args inclusively
    index = random.randint(0, len(copied_array) -1)
    
    # Pop Pivot element
    pivot_element = copied_array.pop(index)
    
    # Declare Subarrays
    # Note: Pivot goes in center
    center_elements_array = [pivot_element]
    smaller_elements_array = []
    bigger_elements_array = []
    
    # Loop through the copiedArray while length not 0:
    while len(copied_array) > 0:
        # Set current_element
        current_element = copied_array.pop()
        
        # Goldilock conditions:
        # Perform Partitioning based on Pivot:
        if current_element == pivot_element:
            center_elements_array.append(current_element)
        # If smaller, push to smaller array
        elif current_element < pivot_element:
            smaller_elements_array.append(current_element)
        # If larger, push to larger array
        elif current_element > pivot_element:
            bigger_elements_array.append(current_element)
    
    # once partitioning complete, sort (smaller & larger array)
    # using a recursive call: 
    # note center only contains pivot
    smaller_elements_sorted_array = sort(smaller_elements_array)
    bigger_elements_sorted_array = sort(bigger_elements_array)

    # Concatenate all sorted arrays
    return smaller_elements_sorted_array + center_elements_array + bigger_elements_sorted_array
    
numbers = [-3, 10, 1, 100, -10, 22, 15]
sorted_array = sort(numbers)
print(sorted_array)