from collections import deque

# Mnuemonic: Quincy and Greg may list popular cafes if service or quality is amazing.

# Runtime: O(number of edges), if you search and entire network,
# for mango seller, that means you follow each edge (arrow connecting one person to another)

# You also keep a queue of every person to search.  Adding one person to the queue
# takes constant time.  O(1).  Doing this for every person will take O(number of people)
# total.  

# Depth First Search takes O(number of people + number of edges), commonly written as
# O(V + E) ( V for number of vertices; E for number of edges)

# Create graph:

# Define the graph as a dictionary
# Note: Since a hashtable is an unorderd
# collection it doesn not matter how you
# order the graph
# graph = {
#     "you": ["alice", "bob", "claire"],
#     "alice": ["peggy"],
#     "bob": ["anuj", "peggy"],
#     "claire": ["thom", "jonny"],
#     "anuj": [],
#     "peggy": [],
#     "thom": [],
#     "jonny": []
# }

graph = {
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    
}

#  Function telling if peron is mango seller
def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    # Create a new queue, which searches for people in the order they were added
    # Queue (Quincy)
    search_queue = deque()
    # Add (*And Graph*) all your out-neighbor (graph item values) to the queue individually
    search_queue += graph[name]
    print("Search Queue:", search_queue)
    
    # Memoization (*May*): Keep track of which people you've searched before.
    # Use set so we do not collect duplicates           
    searched = set()

    # Loop (*List*) queue is not empty
    while search_queue:
        # Pop (*Popular*) the first person of the queue
        person = search_queue.popleft()
        print("person:", person)
        # Memoization: Do not check person who has already been searched
        # Note: The people who appear in the searched set:
        # Conditionals (Cafes)
        if not person in searched:
            # Check if person is mango seller (*If Service*)
            if person_is_seller(person):
                # if mango seller print
                print(person + ' is a mango seller!')
                return True
            # Add name to queue(Or quality)
            else:
                # IF not mango seller, add persons friends to search_queue.
                search_queue += graph[person]
                
            # Add person (*Is AMAZING*) to search_queue set each time they have been searched
            searched.add(person)
    # No one is a mango seller
    return False

# Call Search:
search('you')

