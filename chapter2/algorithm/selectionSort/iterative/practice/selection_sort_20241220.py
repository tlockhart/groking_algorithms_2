# I Saw Interesting Fans To Sell
# O(n^2)
def findSmallest(items):
    # Iniatialize smallest
    smallest_idx = 0
    
    # find the smallest 
    for idx in (range(1, len(items))):
        if items[idx] < items[smallest_idx]:
            smallest_idx = idx
    
    return smallest_idx
        


# I Am Loving Popularity
def selectionSort(items):
    # initialize array
    sorted_array = []
    
    # Loop and pop items
    # O(n)
    while len(items) > 0:
        smallest_idx = findSmallest(items)
        sorted_array.append(items.pop(smallest_idx))
    return sorted_array
      
items = [0, 99, 81, 41, 23, 22, 19, 105]
print("array:", selectionSort(items))  
# Total O(n^2 + n) = n^2