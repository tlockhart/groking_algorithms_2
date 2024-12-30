def count(items):
    # base case
    if len(items) == 0:
        return 0
    elif len(items) == 1:
        return 1
    
    # recursive case:
    items.pop()
    return count(items) + 1

items = [1, 2, 3]
print(count(items))