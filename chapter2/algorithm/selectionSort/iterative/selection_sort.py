# Return the index of the smallest element in arr.

# Note: How we are working with indexes only
# I S I ( I swap ideas)
def findSmallest(arr):
    # Initialize
    smallest = arr[0]
    smallest_index = 0
    length = len(arr)
    print(length)
    
    # Swap
    for i in range(1, length):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    # Return index
    return smallest_index

# Return sorted array
# I L R A ( I Love Repeating Actions)
def selectionSort(arr):
    # Initialize
    newArr = []
    copiedArr = list(arr)
    # Loop
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        print ("Smallest:", smallest)
        # pop() takes an index as an argument. It removes the element at the index of copiedArr
        newArr.append(copiedArr.pop(smallest))
    # Retun sorted array
    return newArr

items = [0, 99, 81, 41, 23, 22, 19, 105]
print(selectionSort(items))

