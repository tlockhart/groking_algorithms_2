def findSmallest(arr):
    # initialize smallest index
    # I S I (I saw interesting)
    smallest = 0
    copied_arr = []
    length = len(arr)
    
    # Find the smallest index
    # F T S ( Fans to sell)
    for i in range(1, len(arr)):
        if arr[i] < arr[smallest]:
            smallest = i
    return smallest

# I Love Repeating actions
def selectionSort(arr):
    # Initialize array
    # I A ( I Am)
    sorted_arr = []
    # Loop and pop array, while it has values
    # L P (Loving Popularity)
    while len(arr) > 0:
        index = findSmallest(arr);
        sorted_arr.append(arr.pop(index))
    return sorted_arr

items = [0, 99, 81, 41, 23, 22, 19, 105]
print("SortedArray:", selectionSort(items))