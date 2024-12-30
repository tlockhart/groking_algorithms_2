# Function to check if the person is a mango seller
def person_is_seller(name):
    last_letter = name[-1]
    print("Last letter:", last_letter)
    value = last_letter == '6'
    print("Value:", value)
    return value
# O(n)
# Mneumonic: SLICER
def search(name):
    print("Checking:", name)

    # C: Check if the current node is the target
    if person_is_seller(name):
        print(name + ' is a mango seller!')
        return True

    # E: Expand search to neighbors
    # Get the values associated with the name key, 
    # then loop through them one at a time
    for neighbor in tree.get(name, []):
        print("Neighbor:", neighbor)
        # Recursive call
        if search(neighbor):  
            return True

    # R: Return False if no seller found in this path
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