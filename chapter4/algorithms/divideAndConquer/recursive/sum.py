def sum(items):
    # base case
    if len(items) == 0:
        return 0
    elif len(items) == 1:
        return items[0]
    
    # It is best not to pop the items
    # n = items.pop()
    n = items[0]
    # return n + sum(items)
    return n + sum(items[1:])

items = [1,2,3]
print(sum(items))