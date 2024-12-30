def findSmallest(items):
    # I Saw Interesting (init small index)
    smallest = 0
    
    # Fans to Sell ( Find the smallest index)
    for i in range(1, len(items)):
        if items[i] < items[smallest]:
            smallest = i
    return smallest

def selectionSort(items):
    # I am ( Init array)
    sorted_array = []
    # Loving Popularity (Loop and pop array):
    while len(items) > 0:
        index = findSmallest(items);
        sorted_array.append(items.pop(index))
    return sorted_array

items = [0, 99, 81, 41, 23, 22, 19, 105]
print("Sorted Array:", selectionSort(items))