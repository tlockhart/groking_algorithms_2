# I saw interesting, fans to sell

def findSmallest(numbers):
    # initialize smallest index
    smallest = 0
    # find the smallest with swap
    for idx in range(1, len(numbers)):
        if numbers[idx] < numbers[smallest]:
            smallest = idx
    return smallest

# I Am Loving Popularity

def selectionSort(numbers):
    #initilze low
    sorted_array = []
    
    while len(numbers) > 0:
        smallest = findSmallest(numbers)
        # print("Smallest:", smallest)
        sorted_array.append(numbers.pop(smallest));
    return sorted_array

numbers = [9, 0, 1, 4]
print(selectionSort(numbers))

    