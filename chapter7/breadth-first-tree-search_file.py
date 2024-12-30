from os import listdir
from os.path import isfile, join
from collections import deque
# Note: We do not need a searched memoization set, to check 
# if we have visited a node, because trees do not cycle
def printnames(start_dir):
    # Queue keeps track of folders to search
    search_queue = deque()
    search_queue.append(start_dir)
    # While queue is not empty, pop off a folder to look through
    while search_queue:
        dir = search_queue.popleft()
        # Loop through every file and folder in this popped folder
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            # if the folder is a file, then print out the name
            if isfile(fullpath):
                print(file)
            else:
                # if it is a folder, add it to the queue of folders to search
                search_queue.append(fullpath)
printnames("pics")