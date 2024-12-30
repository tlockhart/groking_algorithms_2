# Mneumonic: Quincey and Greg may list popular cafes if service or quality is awesome.
from collections import deque


# Dictionary
graph = {
    "you": ["boby", "alice", "claire"],
    "alice": ["peggy"],
    "boby": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "thom": [],
    "jonny": [],
    "peggy": [],
         }

def is_seller(name):
    if name[-1] == "m":
        return True
    
def search(name):
    # Quincy (Queue)
    search_queue = deque()
    
    # And Greg (Add Graph)
    # Appends the whole list element as a single element
    # for name in graph:
    #     search_queue.append(graph[name])
    
    # Appends the spreaded value of the list
    search_queue += graph.get(name)
    print("Search Queue", search_queue)
    # (May) Memoization
    searched = set()
    
    # (List) Loop until no more values in search_queue
    while len(search_queue) > 0:
        # Popular (Pop the first item off search_q ['boby', 'alice'])
        name = search_queue.popleft()
        print("name:", name)
        # Cafe (Conditionals)
        if name not in searched:
            # If service
            if is_seller(name):
                print(f'{name} is seller!')
                # FOUND CONDITON END LOOP
                return True
                
            # Or Quality (Search Queue)
            else:
                search_queue += graph[name]
    # Awesome (Add)
    searched.add(name)    
    
    return False

search('you')