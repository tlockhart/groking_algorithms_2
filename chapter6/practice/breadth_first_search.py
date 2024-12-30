from collections import deque

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

def is_seller(name):
    if name[-1] == "m":
        return True
    
# Quincy and Greg may list popular cafes, if service or quality is awesome
def search(name):
    # Queue
    search_queue = deque()
    # Add graph (GREG) list element to search_queue, with items spread
    search_queue += graph[name]
    # memo
    searched = set()
    # Loop
    while search_queue:
        person = search_queue.popleft()
        # Pop Conditon
        if person not in searched:
            # Is Seller
            if is_seller(person):
                print(f'{person} is seller')
                return True
            else:
                # add search_queue (Quality)
                search_queue += graph[person]
        # Is awesome (Add person)
        searched.add(person)
    return False
            
search('you')