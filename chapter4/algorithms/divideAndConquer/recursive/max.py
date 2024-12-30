def max(items):
    # base case:
    if len(items) == 0:
        return 0
    elif len(items) == 1:
        return items[0]
    # its best to slice to get a copy, instead of modifying the array
    # largest = items.pop()
    largest = items[0]
    # next_item = max(items)
    next_item = max(items[1:])
    if largest > next_item:
        return largest
    else:
        return next_item
    
items = [1,2,3]
print(max(items))