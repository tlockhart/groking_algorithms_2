from collections import deque

graph = {
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"]
}

#Use a set to make sure we do not check an item twice
searched = set()

def find_duplicate(items):
    # Unpack elements in the dictionary
    search_queue = deque([*graph.values()])
    for item in search_queue:
        print("Item:", item)
        
        if len(item) >= 1: 
            # List Comprehension: Filter out items
            # that are in the searched list
            filtered_list = [x for x in item if x not in searched]
            
            # Loop through on names that have not
            # been added to the searched list
            for name in filtered_list:    
                print("Name:", name)
                # If name has been search
                # Add to searched list
                searched.add(name)
                print("Searched:", searched)
        
find_duplicate(graph)