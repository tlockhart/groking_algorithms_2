from collections import deque

graph = {
    "you": ["sam", "jack"],
    "sam": [ "tod", "boby"],
    "jack": [],
    "tod": [],
    "boby": []
}

def is_seller(name):
    if name[-1] == "m":
        # print(f'{name} is a seller')
        return True

# Quincy and Greg may list popluar cafes, if service or quality is awesome
def search_string(name):
    # Queue
    search_queue = deque()
    # Add graph[name] item to search_queue
    search_queue += graph[name]
    
    # Memo
    searched = set()
    
    # Loop
    while search_queue:
        # pop
        person = search_queue.popleft()
        # Condition
        if person not in searched:
            # if seller
            if is_seller(person):
                print(f"{person} is a seller")
            # or quality
            else:
             search_queue += graph[person]  
        searched.add(person)
    return False

search_string("you")
    
    
    