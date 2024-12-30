
def is_seller(name):
    if name[-1] == "6":
        return True
    
# SLICER:
def search(name):
    # S initialize search_stack
    search_stack = [name]
    
    # L: Part1: Loop
    while search_stack:
        # I init person
        person = search_stack.pop()
        
        # C Check Condition:
        if is_seller(person):
            print(person, "is seller")
            return True
        
        # E Part2: Expand the search tree
        neighbors = tree.get(person, [])
        for i in range(len(neighbors) -1, -1, -1):
            search_stack.append(neighbors[i])
    # Return false
    return False
    
    
    
    
    
    
    
    
# Tree/Graph structure as dictionary
    #                                            Person
    #                                               |
    #                          -----------------------------------------
    #                         /                                         \
    #               Parent1                                              Parent2
    #            /          \                                         /                \
    #  Grandparent1           Grandparent2                     Grandparent3           Grandparent4
    #            /  \                /    \                      /   \                     /   \
    # GreatGrand1  GreatGrand2 GreatGrand3 GreatGrand4  GreatGrand5  GreatGrand6  GreatGrand7 GreatGrand8


tree = {
    "you": ["Parent1", "Parent2"],
    "Parent1": ["Grandparent1", "Grandparent2"],
    "Parent2": ["Grandparent3", "Grandparent4"],
    "Grandparent1": ["GreatGrand1", "GreatGrand2"],
    "Grandparent2": ["GreatGrand3", "GreatGrand4"],
    "Grandparent3": ["GreatGrand5", "GreatGrand6"],
    "Grandparent4": ["GreatGrand7", "GreatGrand8"],
    "GreatGrand1": [],
    "GreatGrand2": [],
    "GreatGrand3": [],
    "GreatGrand4": [],
    "GreatGrand5": [],
    "GreatGrand6": [],
    "GreatGrand7": [],
    "GreatGrand8": []
}

# Call Search starting from "you"
search('you')

# print(is_seller("you"))