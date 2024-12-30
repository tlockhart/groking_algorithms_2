# Function to check if the person is a mango seller
def person_is_seller(name):
    last_letter = name[-1]
    print("Last letter:", last_letter)
    value = last_letter == '6'
    print("Value:", value)
    return value
# O(n)
# Mneumonic: SLICER (starts on left side of tree, since we are using a stack(LIFO))
def search(name):
    """
    Performs a depth-first search on a tree to find a mango seller.

    Args:
      name: The name of the starting node.

    Returns:
      True if a mango seller is found, False otherwise.
    """

    # S: Start with the stack
    # the stack is processed in a Last In First Out (LIFO) order. 
    # This means that when you add neighbors to the stack, they 
    # are processed in the reverse order of their addition 
    # (i.e., the rightmost neighbor will be processed first).
    # To reverse, you have to add the children to the search_stack
    # in reverse order
    search_stack = [name]
    print("Search Stack:", search_stack)

    # L: Part 1: Loop through while there are items in the stack
    while search_stack:
        # I: Inspect the current node, pop off last value, 
        # it only has "you"
        person = search_stack.pop()
        print("Person:", person)

        # C: Check if the current node is the target
        if person_is_seller(person):
            print(person + ' is a mango seller!')
            return True

        # E: Part 2: Expand by adding neighbors to the stack (left-to-right)
        neighbors = tree.get(person, []) 
        # Reverse the order of the neighbors:
        # Iterate in reverse order using indices
        # range(lastIndex, stop value, step)
        for i in range(len(neighbors) - 1, -1, -1):  
            search_stack.append(neighbors[i]) 

    # R: Return False when the stack is empty
    print("No mango seller found!")
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